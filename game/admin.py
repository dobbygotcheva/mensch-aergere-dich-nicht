from django.contrib import admin
from .models import Game, Player, Piece


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'current_player_index', 'winner', 'created_at']
    list_filter = ['status', 'created_at']


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'color', 'game', 'order']
    list_filter = ['color', 'game']


@admin.register(Piece)
class PieceAdmin(admin.ModelAdmin):
    list_display = ['id', 'player', 'piece_number', 'position', 'in_home']
    list_filter = ['player', 'in_home']

