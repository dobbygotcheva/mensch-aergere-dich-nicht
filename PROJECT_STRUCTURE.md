# Mensch, ärgere dich nicht! - Project Structure

## 📁 Project Overview

A Django-based web implementation of the classic board game "Mensch, ärgere dich nicht!" (Don't b mad, man!) with a modern purple/pink themed UI.

---

## 🗂️ Directory Structure

```
PycharmProjects/PythonProject1/
│
├── dont_b_mad/                 # Main Django project directory
│   ├── __init__.py
│   ├── asgi.py                 # ASGI configuration
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Main URL routing
│   └── wsgi.py                 # WSGI configuration
│
├── game/                        # Main game application
│   ├── migrations/             # Database migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_piece_steps_taken.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py                # Django admin configuration
│   ├── apps.py                 # App configuration
│   ├── currency_mapping.py     # Team/currency theme mappings
│   ├── models.py               # Database models (Game, Player, Piece)
│   ├── special_tasks.py        # Challenge tasks for special positions
│   ├── urls.py                 # Game URL patterns
│   └── views.py                # View functions and game logic
│
├── templates/                   # HTML templates
│   ├── base.html               # Base template (navbar, footer)
│   └── game/
│       ├── home.html           # Home page with purple/pink gradient
│       ├── create_game.html    # Game creation form
│       └── game_board.html     # Main game board interface
│
├── static/                      # Static files
│   ├── css/
│   │   └── style.css           # Main stylesheet
│   ├── js/
│   │   ├── game.js             # Game interaction logic
│   │   └── position-visualizer.js  # Board position visualization
│   ├── images/
│   │   ├── dollar/             # USD currency images (Red team)
│   │   ├── euro/               # EUR currency images (Blue team)
│   │   ├── leva/               # BGN currency images (Green team)
│   │   ├── liri/               # Turkish Lira images (Yellow team)
│   │   ├── roma/               # Roman coins (Yellow corner decoration)
│   │   ├── challenges/         # Challenge task images
│   │   ├── dice/               # Dice animation frames (dice1-6.png)
│   │   ├── team1/              # Ninja Turtles (Red)
│   │   ├── team2/              # Philosophen (Blue)
│   │   ├── team3/              # Musicians (Green)
│   │   └── team4/              # Tigers (Yellow)
│   └── favicon.ico             # Dice emoji favicon
│
├── Man-Don-t-Get-Angry-Board-game-main/  # Hardware project reference
│   └── SkaliranePozicije.txt  # Board position coordinates
│
├── db.sqlite3                   # SQLite database
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## 🎮 Core Components

### 1. **Models** (`game/models.py`)

#### Game Model
- Manages game state (waiting, in_progress, finished)
- Tracks current player turn
- Handles dice rolls
- Checks for winners

#### Player Model
- Represents each player in a game
- Assigned colors: Red, Blue, Green, Yellow
- Linked to team themes

#### Piece Model
- Represents game pieces (4 per player)
- Tracks position on board (-1 = start, 0-39 = main path, 40-55 = home)
- Tracks total steps taken for correct home entry
- Handles movement logic and capturing

### 2. **Views** (`game/views.py`)

- **`home()`** - Display home page with active games
- **`create_game()`** - Create new game with 4 players
- **`game_board()`** - Render game board with all game state
- **`roll_dice()`** - Handle dice rolling and determine movable pieces
- **`move_piece()`** - Execute piece movement and check for special tasks
- **`get_game_state()`** - Return current game state as JSON
- **`quit_game()`** - End game and mark as finished

### 3. **Special Features**

#### Currency/Team Mapping (`currency_mapping.py`)
- Maps player colors to team themes
- Red → Ninja Turtles (Dollar)
- Blue → Philosophen (Euro)
- Green → Musicians (Leva)
- Yellow → Tigers (Roma)

#### Special Tasks (`special_tasks.py`)
- 10 unique Bulgarian-themed challenges
- Distributed across all board sections
- Tasks include: singing, dancing, impersonations, etc.
- Displayed in modal popup when landing on special positions

### 4. **Frontend** (`static/js/game.js`)

- Dice rolling animation with image cycling
- Piece movement and positioning
- AJAX calls for game state updates
- Special task modal display
- Team character images for pieces

### 5. **Styling** (`static/css/style.css`)

- **Theme:** Purple/pink gradient (#667eea → #764ba2 → #f093fb)
- **Colors:**
  - Text: Warm cream (#fef3e2, #f5e6d3)
  - Backgrounds: Purple rgba(118, 75, 162, ...)
  - Borders: Pink rgba(240, 147, 251, ...)
- **Effects:**
  - Frosted glass (backdrop-filter: blur)
  - Smooth animations and transitions
  - Drop shadows for depth
  - Hover effects (lift, scale, glow)

---

## 🎨 Design Theme

### Color Palette
- **Background Gradient:** Purple → Pink
- **Text:** Warm Cream/Beige
- **Borders:** Pink accents
- **Player Colors:** Red, Blue, Green, Yellow

### Visual Effects
- Frosted glass panels
- Drop shadows
- Smooth animations
- Hover interactions
- Dice roll animation
- Floating decorations on home page

---

## 🎲 Game Logic Flow

1. **Create Game** → Creates game with 4 players
2. **Roll Dice** → Player rolls 1-6
3. **Select Piece** → Click movable piece (highlighted)
4. **Move Piece** → Piece moves on board
5. **Check Special Position** → Display task if applicable
6. **Check Capture** → Send opponent pieces back to start
7. **Check Winner** → All 4 pieces in home = win
8. **Next Turn** → Move to next player

---

## 📊 Database Schema

### Game Table
- id, created_at, status, current_player_index, winner_id, dice_value

### Player Table
- id, game_id, user_id, name, color, order

### Piece Table
- id, player_id, piece_number (0-3), position (-1 to 55), in_home, steps_taken

---

## 🚀 Key Features

1. ✅ Full game logic implementation
2. ✅ Purple/pink themed UI
3. ✅ Currency-themed board decorations
4. ✅ Team character pieces
5. ✅ Special challenge tasks
6. ✅ Dice rolling animation
7. ✅ Responsive design
8. ✅ Real-time game updates
9. ✅ Piece capture mechanics
10. ✅ Win condition checking

---

## 🔧 Technical Stack

- **Backend:** Django 4.2.11
- **Database:** SQLite3
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Graphics:** SVG for game board
- **Animations:** CSS keyframes + JavaScript

---

## 📝 Notes

- Board coordinates derived from hardware project (SkaliranePozicije.txt)
- 40-position circular main path
- 16 home lane positions (4 per player)
- Challenge tasks at specific positions across all sections
- Piece movement uses `steps_taken` for accurate home entry after 40 steps

---

## 🎯 Future Enhancements (Optional)

- Online multiplayer
- Player accounts and authentication
- Game history/statistics
- Mobile responsive optimization
- Sound effects
- Tournament mode

