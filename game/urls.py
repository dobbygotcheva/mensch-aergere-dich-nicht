from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_game, name='create_game'),
    path('game/<int:game_id>/', views.game_board, name='game_board'),
    path('game/<int:game_id>/roll/', views.roll_dice, name='roll_dice'),
    path('game/<int:game_id>/move/<int:piece_id>/', views.move_piece, name='move_piece'),
    path('game/<int:game_id>/state/', views.get_game_state, name='game_state'),
    path('game/<int:game_id>/quit/', views.quit_game, name='quit_game'),
]

