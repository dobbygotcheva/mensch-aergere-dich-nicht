"""
Special Tasks Module
====================

Defines challenge tasks for special board positions.

Features:
    - 10 unique Bulgarian-themed challenges
    - Distributed across all board sections
    - Various task types: performance, physical, knowledge, creative
    - Each task has title, description, type, and image

Task Distribution:
    - Red section (0-9): Positions 3, 7
    - Blue section (10-19): Positions 13, 17, 19
    - Green section (20-29): Positions 22, 26
    - Yellow section (30-39): Positions 33, 37, 39

Author: Mensch, ärgere dich nicht! Team
Date: October 2025
"""


# =============================================================================
# SPECIAL CHALLENGE TASKS
# =============================================================================

# Special Challenge tasks spread across ALL sections
# Distributed evenly so all players encounter them throughout the game!

SPECIAL_TASKS = {
    # Red section challenges (0-9)
    3: {
        'title': 'Bai Ganio! 📖',
        'task': 'Read a passage from Bai Ganio or tell us something about Bulgarian literature!',
        'type': 'knowledge',
        'image': 'challenges/бай_ganio.jpg'
    },
    7: {
        'title': 'Catwalk! 👠',
        'task': 'Do a catwalk strut across the room like a fashion model!',
        'type': 'challenge',
        'image': 'challenges/catwalk.jpg'
    },
    
    # Blue section challenges (10-19)
    13: {
        'title': 'Dance Challenge! 💃',
        'task': 'Show us your best dance moves for 10 seconds!',
        'type': 'challenge',
        'image': 'challenges/dance.jpg'
    },
    17: {
        'title': 'Burgas 63! 🍷',
        'task': 'Take a sip of rakia (or pretend to) and say "Nazdrave!"',
        'type': 'challenge',
        'image': 'challenges/Burgas_63.jpg'
    },
    19: {
        'title': 'Light Weight! 💪',
        'task': 'Do 20 push-ups or lose your next turn!',
        'type': 'challenge',
        'image': 'challenges/light weight.png'
    },
    
    # Green section challenges (20-29)
    22: {
        'title': 'Dictionary Time! 📚',
        'task': 'Say a phraseologism from the dictionary of Professor Stantcheva!',
        'type': 'knowledge',
        'image': 'challenges/dictionary.jpeg'
    },
    26: {
        'title': 'Hot Peppers! 🌶️',
        'task': 'Eat a hot pepper or go back 3 spaces!',
        'type': 'challenge',
        'image': 'challenges/hot pepper.jpg'
    },
    
    # Yellow section challenges (30-39)
    33: {
        'title': 'Luft Anhalten! 🌬️',
        'task': 'Hold your breath for 30 seconds!',
        'type': 'challenge',
        'image': 'challenges/luft_anhalten.png'
    },
    37: {
        'title': 'Music Break! 🎵',
        'task': 'Sing us a song (at least 30 seconds)!',
        'type': 'challenge',
        'image': 'challenges/music break.png'
    },
    39: {
        'title': 'Radoi Ralin! ✍️',
        'task': 'Write a short poem (4 lines) right now!',
        'type': 'challenge',
        'image': 'challenges/radoi_ralin.jpg'
    }
}

def get_task(position):
    """Get the special task for a position"""
    if position in SPECIAL_TASKS:
        return SPECIAL_TASKS[position]
    return None

def is_special_position(position):
    """Check if a position has a special task"""
    return position in SPECIAL_TASKS

def get_all_special_positions():
    """Get list of all special positions"""
    return list(SPECIAL_TASKS.keys())

