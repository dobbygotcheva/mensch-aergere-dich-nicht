"""
Game Views Module
=================

Handles all HTTP requests and responses for the board game.

Main Functions:
    - home(): Display home page with active games
    - create_game(): Create new game with 4 players
    - game_board(): Render main game interface
    - roll_dice(): Handle dice rolling logic
    - move_piece(): Execute piece movement and special tasks
    - get_game_state(): Return current game state as JSON
    - quit_game(): End game and mark as finished

Author: Mensch, ärgere dich nicht! Team
Date: October 2025
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Game, Player, Piece
from .currency_mapping import CURRENCY_MAPPING
from .special_tasks import get_task, is_special_position, get_all_special_positions
import json


# =============================================================================
# CONFIGURATION - Team Piece Images Mapping
# =============================================================================

# Team piece images mapping - maps each player color to 4 character images
TEAM_PIECE_IMAGES = {
    'red': [
        'team1/Leonardo.jpg',
        'team1/raph.webp',
        'team1/doni.jpeg',
        'team1/mickey.png'
    ],
    'blue': [
        'team2/hegel.jpeg',
        'team2/karl marx.jpeg',
        'team2/nietzsche.jpg',
        'team2/Schopenhauer_by_Jules_Lunteschütz.jpg'
    ],
    'green': [
        'team3/Beethoven.jpg',
        'team3/liszt.jpg',
        'team3/schumann.jpg',
        'team3/todor_kolev.jpg'
    ],
    'yellow': [
        'team4/bengal.jpg',
        'team4/black.jpeg',
        'team4/siberian_tiger.jpg',
        'team4/white-tiger-Bengal.webp'
    ]
}


def home(request):
    """Home page showing available games"""
    games = Game.objects.filter(status__in=['waiting', 'in_progress']).order_by('-created_at')
    return render(request, 'game/home.html', {'games': games})


def create_game(request):
    """Create a new game"""
    if request.method == 'POST':
        game = Game.objects.create(status='waiting')
        
        # Create 4 players with different colors
        colors = ['red', 'blue', 'green', 'yellow']
        player_names = request.POST.getlist('player_names[]')
        
        if not player_names or len(player_names) < 2:
            player_names = ['Player 1', 'Player 2', 'Player 3', 'Player 4']
        
        for i, color in enumerate(colors):
            player_name = player_names[i] if i < len(player_names) else f'Player {i+1}'
            player = Player.objects.create(
                game=game,
                name=player_name,
                color=color,
                order=i
            )
            
            # Create 4 pieces for each player
            for piece_num in range(4):
                Piece.objects.create(
                    player=player,
                    piece_number=piece_num,
                    position=-1  # Start in starting area
                )
        
        game.status = 'in_progress'
        game.save()
        
        return redirect('game_board', game_id=game.id)
    
    return render(request, 'game/create_game.html')


def game_board(request, game_id):
    """Display the game board"""
    game = get_object_or_404(Game, id=game_id)
    players = game.players.all().order_by('order')
    current_player = game.get_current_player()
    
    # Get all pieces for all players with team images
    pieces_data = []
    for player in players:
        currency_info = CURRENCY_MAPPING.get(player.color, {})
        team_imgs = TEAM_PIECE_IMAGES.get(player.color, [])
        for piece in player.pieces.all():
            # Get the specific team image for this piece
            team_image = team_imgs[piece.piece_number] if piece.piece_number < len(team_imgs) else ''
            
            pieces_data.append({
                'id': piece.id,
                'player_color': player.color,
                'position': piece.position,
                'in_home': piece.in_home,
                'piece_number': piece.piece_number,
                'currency': currency_info.get('currency', ''),
                'currency_symbol': currency_info.get('symbol', ''),
                'team_image': team_image,
            })
    
    # Add currency info and team images to players and pieces
    players_with_currency = []
    for player in players:
        player.currency_info = CURRENCY_MAPPING.get(player.color, {})
        player.team_images = TEAM_PIECE_IMAGES.get(player.color, [])
        
        # Attach specific team image to each piece and cache the pieces list
        pieces_list = []
        for piece in player.pieces.all():
            team_imgs = TEAM_PIECE_IMAGES.get(player.color, [])
            if piece.piece_number < len(team_imgs):
                piece.team_image = team_imgs[piece.piece_number]
            else:
                piece.team_image = ''
            pieces_list.append(piece)
        
        # Cache the pieces list with team images
        player.pieces_with_images = pieces_list
        
        players_with_currency.append(player)
    
    context = {
        'game': game,
        'players': players_with_currency,
        'current_player': current_player,
        'pieces_data': json.dumps(pieces_data),
        'currency_mapping': CURRENCY_MAPPING,
        'special_positions': get_all_special_positions(),
    }
    
    return render(request, 'game/game_board.html', context)


@require_POST
def roll_dice(request, game_id):
    """Roll the dice for the current player"""
    game = get_object_or_404(Game, id=game_id)
    
    if game.status != 'in_progress':
        return JsonResponse({'error': 'Game is not in progress'}, status=400)
    
    dice_value = game.roll_dice()
    current_player = game.get_current_player()
    
    # Check which pieces can move
    movable_pieces = []
    if current_player:
        for piece in current_player.pieces.all():
            if piece.can_move(dice_value):
                movable_pieces.append(piece.id)
    
    return JsonResponse({
        'dice_value': dice_value,
        'current_player': current_player.name if current_player else None,
        'current_player_color': current_player.color if current_player else None,
        'movable_pieces': movable_pieces
    })


@require_POST
def move_piece(request, game_id, piece_id):
    """Move a piece on the board"""
    game = get_object_or_404(Game, id=game_id)
    piece = get_object_or_404(Piece, id=piece_id)
    
    if game.status != 'in_progress':
        return JsonResponse({'error': 'Game is not in progress'}, status=400)
    
    current_player = game.get_current_player()
    if piece.player != current_player:
        return JsonResponse({'error': 'Not your turn'}, status=403)
    
    if game.dice_value == 0:
        return JsonResponse({'error': 'Roll the dice first'}, status=400)
    
    if not piece.can_move(game.dice_value):
        return JsonResponse({'error': 'Invalid move'}, status=400)
    
    # Move the piece
    piece.move(game.dice_value)
    
    # Check if landed on a special position (Yellow section)
    special_task = None
    if is_special_position(piece.position):
        special_task = get_task(piece.position)
    
    # Check for winner
    if game.check_winner():
        response = {
            'success': True,
            'piece_position': piece.position,
            'in_home': piece.in_home,
            'game_over': True,
            'winner': game.winner.username if game.winner else current_player.name
        }
        if special_task:
            response['special_task'] = special_task
        return JsonResponse(response)
    
    # Move to next turn (unless rolled a 6, then get another turn)
    if game.dice_value != 6:
        game.next_turn()
    else:
        game.dice_value = 0
        game.save()
    
    # Get all pieces positions for update
    all_pieces = []
    for player in game.players.all():
        for p in player.pieces.all():
            all_pieces.append({
                'id': p.id,
                'position': p.position,
                'in_home': p.in_home,
                'player_color': p.player.color
            })
    
    next_player = game.get_current_player()
    
    response = {
        'success': True,
        'all_pieces': all_pieces,
        'next_player': next_player.name if next_player else None,
        'next_player_color': next_player.color if next_player else None,
        'game_over': False
    }
    
    if special_task:
        response['special_task'] = special_task
    
    return JsonResponse(response)


def get_game_state(request, game_id):
    """Get the current state of the game"""
    game = get_object_or_404(Game, id=game_id)
    current_player = game.get_current_player()
    
    pieces_data = []
    for player in game.players.all():
        for piece in player.pieces.all():
            pieces_data.append({
                'id': piece.id,
                'player_color': player.color,
                'position': piece.position,
                'in_home': piece.in_home,
                'piece_number': piece.piece_number
            })
    
    return JsonResponse({
        'status': game.status,
        'current_player': current_player.name if current_player else None,
        'current_player_color': current_player.color if current_player else None,
        'dice_value': game.dice_value,
        'pieces': pieces_data,
        'winner': game.winner.username if game.winner else None
    })


@require_POST
def quit_game(request, game_id):
    """End/quit the current game"""
    try:
        game = get_object_or_404(Game, id=game_id)
        
        # Mark game as finished
        game.status = 'finished'
        game.save()
        
        return JsonResponse({
            'success': True,
            'message': 'Game ended successfully'
        })
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=400)

