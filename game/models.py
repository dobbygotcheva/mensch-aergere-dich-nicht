from django.db import models
from django.contrib.auth.models import User
import json
import random


class Game(models.Model):
    """Represents a game instance of Don't b mad, man!"""
    STATUS_CHOICES = [
        ('waiting', 'Waiting for Players'),
        ('in_progress', 'In Progress'),
        ('finished', 'Finished'),
    ]
    
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')
    current_player_index = models.IntegerField(default=0)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='won_games')
    dice_value = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Game {self.id} - {self.status}"
    
    def get_current_player(self):
        """Get the current player whose turn it is"""
        players = list(self.players.all().order_by('order'))
        if players:
            return players[self.current_player_index % len(players)]
        return None
    
    def roll_dice(self):
        """Roll a dice and return the value"""
        self.dice_value = random.randint(1, 6)
        self.save()
        return self.dice_value
    
    def next_turn(self):
        """Move to the next player's turn"""
        player_count = self.players.count()
        if player_count > 0:
            self.current_player_index = (self.current_player_index + 1) % player_count
            self.dice_value = 0
            self.save()
    
    def check_winner(self):
        """Check if any player has won the game"""
        for player in self.players.all():
            if player.has_won():
                self.winner = player.user
                self.status = 'finished'
                self.save()
                return True
        return False


class Player(models.Model):
    """Represents a player in a game"""
    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
    ]
    
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='players')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        unique_together = ['game', 'order']
    
    def __str__(self):
        return f"{self.name} ({self.color})"
    
    def has_won(self):
        """Check if this player has won (all 4 pieces in home)"""
        pieces = self.pieces.all()
        return len(pieces) == 4 and all(piece.in_home for piece in pieces)


class Piece(models.Model):
    """Represents a game piece for a player"""
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='pieces')
    piece_number = models.IntegerField()  # 0-3 for each player
    position = models.IntegerField(default=-1)  # -1 means in start area, 0-39 on board, 40-55 in home
    in_home = models.BooleanField(default=False)
    steps_taken = models.IntegerField(default=0)  # Track total steps taken from start position
    
    class Meta:
        unique_together = ['player', 'piece_number']
    
    def __str__(self):
        return f"{self.player.name}'s Piece {self.piece_number + 1}"
    
    def is_in_start(self):
        """Check if piece is still in starting area"""
        return self.position == -1
    
    def can_move(self, dice_value):
        """Check if this piece can move with the given dice value"""
        # Can only leave start with a 6
        if self.is_in_start():
            return dice_value == 6
        
        # Can't move if already in home
        if self.in_home:
            return False
        
        # Calculate where piece would end up
        if self.position < 40:  # On main path
            new_pos = self._calculate_new_position(dice_value)
            if new_pos is None:
                return False
        else:  # In home lane
            new_position = self.position + dice_value
            # Each player has 4 home positions
            color_home_ranges = {'red': (40, 43), 'blue': (44, 47), 'green': (48, 51), 'yellow': (52, 55)}
            home_range = color_home_ranges.get(self.player.color, (40, 43))
            if new_position > home_range[1]:
                return False
        
        return True
    
    def _calculate_new_position(self, dice_value):
        """Calculate new position after moving, handling circular path and home entry"""
        color_config = {
            'red': {'start': 0, 'home_start': 40},
            'blue': {'start': 10, 'home_start': 44},
            'green': {'start': 20, 'home_start': 48},
            'yellow': {'start': 30, 'home_start': 52}
        }
        
        config = color_config.get(self.player.color)
        if not config:
            return None
        
        # Calculate new steps and position
        new_steps = self.steps_taken + dice_value
        
        # If we've completed 40 steps, we should be entering home
        if new_steps >= 40:
            steps_into_home = new_steps - 40
            # Check if we've passed the 4 home positions
            if steps_into_home > 3:
                return None  # Can't move past home
            return (config['home_start'] + steps_into_home, new_steps)
        
        # Otherwise, continue on main path (circular)
        new_position = (config['start'] + new_steps) % 40
        return (new_position, new_steps)
    
    def move(self, dice_value):
        """Move the piece by the dice value"""
        if not self.can_move(dice_value):
            return False
        
        # Moving from start
        if self.is_in_start():
            if dice_value == 6:
                # Get starting position based on player color
                color_starts = {'red': 0, 'blue': 10, 'green': 20, 'yellow': 30}
                self.position = color_starts.get(self.player.color, 0)
                self.steps_taken = 0
                self.save()
                return True
            return False
        
        # Calculate new position
        if self.position < 40:  # On main path
            result = self._calculate_new_position(dice_value)
            if result is None:
                return False
            new_pos, new_steps = result
            self.position = new_pos
            self.steps_taken = new_steps
            
            # Check if we've entered home
            color_home_starts = {'red': 40, 'blue': 44, 'green': 48, 'yellow': 52}
            home_start = color_home_starts.get(self.player.color, 40)
            
            if self.position >= home_start:
                self.in_home = True
        else:  # Already in home lane, just move forward
            self.position += dice_value
            self.steps_taken += dice_value
        
        self.save()
        
        # Check for capturing other pieces (only on main path)
        if not self.in_home:
            self.check_capture()
        
        return True
    
    def check_capture(self):
        """Check if this piece has captured any opponent pieces"""
        if self.in_home or self.is_in_start():
            return
        
        # Find all other pieces at the same position
        other_pieces = Piece.objects.filter(
            player__game=self.player.game,
            position=self.position
        ).exclude(id=self.id).exclude(player=self.player)
        
        # Send them back to start
        for piece in other_pieces:
            if not piece.in_home:
                piece.position = -1
                piece.save()

