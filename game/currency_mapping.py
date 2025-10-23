"""
Currency/Team Mapping Module
=============================

Maps player colors to team themes with associated currency imagery.

Teams:
    - Red → Ninja Turtles (Dollar/USD)
    - Blue → Philosophen (Euro/EUR)
    - Green → Musicians (Leva/BGN)
    - Yellow → Tigers (Roma/Ancient Roman coins)

Each team has:
    - Currency symbol
    - Team name
    - Piece images (currency bills)
    - Small coin images (for board)
    - Large bill images (for home lanes)

Author: Mensch, ärgere dich nicht! Team
Date: October 2025
"""


# =============================================================================
# TEAM TO PLAYER COLOR MAPPING
# =============================================================================

# Maps each player color to a team theme with currency visuals
CURRENCY_MAPPING = {
    'red': {
        'currency': 'dollar',
        'symbol': '$',
        'name': 'Ninja Turtles',
        'piece_image': 'dollar/dollar5.jpg',
        'small_coin': 'dollar/cent1.png',
        'large_bill': 'dollar/dollar100.jpg',
    },
    'blue': {
        'currency': 'euro',
        'symbol': '€',
        'name': 'Philosophen',
        'piece_image': 'euro/5euro',
        'small_coin': 'euro/1cent.png',
        'large_bill': 'euro/100euro.jpeg',
    },
    'green': {
        'currency': 'leva',
        'symbol': 'лв',
        'name': 'Musicians',
        'piece_image': 'leva/5lv.jpg',
        'small_coin': 'leva/st.png',
        'large_bill': 'leva/100lv.jpg',
    },
    'yellow': {
        'currency': 'roma',
        'symbol': '⚜️',
        'name': 'Tigers',
        'piece_image': 'roma/rimska-zlatna-moneta.jpg',
        'small_coin': 'roma/domna-1.jpg',
        'large_bill': 'roma/rimska-zlatna-moneta.jpg',
    }
}

def get_currency_for_player(color):
    """Get currency info for a player color"""
    return CURRENCY_MAPPING.get(color, {})

def get_piece_image(color):
    """Get the piece image path for a player color"""
    currency = get_currency_for_player(color)
    return currency.get('piece_image', '')

