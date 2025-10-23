# Configuration Guide

## 🎨 Theme Configuration

### Color Scheme
Located in templates and CSS files:

```css
/* Main Colors */
--color-red: #ef5350       /* Red player */
--color-blue: #42a5f5      /* Blue player */
--color-green: #66bb6a     /* Green player */
--color-yellow: #ffee58    /* Yellow player */

/* Theme Colors */
Background Gradient: #667eea → #764ba2 → #f093fb
Text: #fef3e2 (warm cream)
Borders: rgba(240, 147, 251, 0.4) (pink)
Panels: rgba(118, 75, 162, 0.3) (purple)
```

---

## 🏷️ Team Configuration

Edit `game/currency_mapping.py`:

```python
CURRENCY_MAPPING = {
    'red': {
        'currency': 'dollar',
        'symbol': '$',
        'name': 'Ninja Turtles',
        'piece_image': 'dollar/dollar5.jpg',
        'small_coin': 'dollar/cent1.png',
        'large_bill': 'dollar/dollar100.jpg',
    },
    # ... other teams
}
```

---

## 🎯 Special Tasks Configuration

Edit `game/special_tasks.py`:

```python
SPECIAL_POSITIONS = {
    3: {
        'task': 'Sing Bulgarian folk song',
        'type': 'performance',
        'icon': '🎤',
        'image': 'challenges/bai_ganio.jpg'
    },
    # ... other positions
}
```

### Task Types:
- `performance` - Singing, dancing
- `physical` - Exercise, movements
- `knowledge` - Trivia, naming
- `creative` - Impersonations, acting

---

## 🎲 Game Rules Configuration

Located in `game/models.py`:

### Piece Movement
```python
# Starting positions by color
color_starts = {
    'red': 0,      # Position 0
    'blue': 10,    # Position 10
    'green': 20,   # Position 20
    'yellow': 30   # Position 30
}

# Home lane positions
color_home_ranges = {
    'red': (40, 43),    # 4 positions
    'blue': (44, 47),   # 4 positions
    'green': (48, 51),  # 4 positions
    'yellow': (52, 55)  # 4 positions
}
```

### Game Rules
- Roll 6 to exit start area
- Complete 40 steps on main path before entering home
- 4 home positions per player
- Exact roll needed to enter final home position
- Capturing: Landing on opponent sends them back to start

---

## 🖼️ Image Configuration

### Required Image Directories

```
static/images/
├── dollar/     - USD currency (Red team coins/bills)
├── euro/       - EUR currency (Blue team coins/bills)
├── leva/       - BGN currency (Green team coins/bills)
├── liri/       - TRY currency (Yellow team coins/bills)
├── roma/       - Roman coins (Yellow corner decoration)
├── challenges/ - Task challenge images (10 images)
├── dice/       - dice1.png to dice6.png (6 images)
├── team1/      - Ninja Turtles (4 images)
├── team2/      - Philosophen (4 images)
├── team3/      - Musicians (4 images)
└── team4/      - Tigers (4 images)
```

### Team Images Configuration

Edit `game/views.py`:

```python
TEAM_PIECE_IMAGES = {
    'red': [
        'team1/Leonardo.jpg',
        'team1/raph.webp',
        'team1/doni.jpeg',
        'team1/mickey.png'
    ],
    # ... other teams (4 images each)
}
```

---

## 🎮 Board Configuration

### Board Positions
Positions are defined in `static/js/game.js`:

```javascript
const boardPositions = {
    0: { x: 225.68, y: 300 },    // Red start
    10: { x: 300, y: 135.52 },   // Blue start
    20: { x: 464.48, y: 300 },   // Green start
    30: { x: 300, y: 464.48 },   // Yellow start
    // ... 40 total positions
};
```

Derived from hardware project coordinates (SkaliranePozicije.txt)

---

## 🔧 Django Settings

Located in `dont_b_mad/settings.py`:

### Database
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Static Files
```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

### Templates
```python
TEMPLATES = [{
    'DIRS': [BASE_DIR / 'templates'],
    # ...
}]
```

---

## 🎨 UI Customization

### Home Page
Edit `templates/game/home.html`:
- Background gradient
- Floating decorations (6 items)
- Team badges
- Button styles

### Game Board
Edit `templates/game/game_board.html`:
- Board size: 700px (adjustable in CSS)
- Sidebar widths: 200px (left), 250px (right)
- Currency coin sizes: 40x40px
- Challenge image sizes: 40-45px

### Create Game Page
Edit `templates/game/create_game.html`:
- Card width: 600px max
- Input field styling
- Animation timing delays

---

## 📊 Performance Configuration

### Dice Animation
Located in `static/js/game.js`:

```javascript
function animateDiceRoll(finalValue, duration = 600) {
    const interval = 50; // Change image every 50ms
    // ...
}
```

### Modal Auto-Close
```javascript
setTimeout(() => {
    hideSpecialTask();
}, 15000); // 15 seconds
```

---

## 🌐 URL Configuration

Located in `game/urls.py`:

```python
urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_game, name='create_game'),
    path('game/<int:game_id>/', views.game_board, name='game_board'),
    path('game/<int:game_id>/roll/', views.roll_dice, name='roll_dice'),
    path('game/<int:game_id>/move/<int:piece_id>/', views.move_piece, name='move_piece'),
    path('game/<int:game_id>/state/', views.get_game_state, name='game_state'),
    path('game/<int:game_id>/quit/', views.quit_game, name='quit_game'),
]
```

---

## 🔐 Security Settings

Currently configured for development:

```python
DEBUG = True
ALLOWED_HOSTS = []
SECRET_KEY = 'django-insecure-...'
```

⚠️ **For Production:**
- Set `DEBUG = False`
- Update `ALLOWED_HOSTS`
- Use environment variable for `SECRET_KEY`
- Configure HTTPS
- Set up proper database (PostgreSQL)

---

## 📝 Logging Configuration

Add to `settings.py` for debugging:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
```

---

## 🚀 Deployment Checklist

1. [ ] Set `DEBUG = False`
2. [ ] Configure `ALLOWED_HOSTS`
3. [ ] Set up production database
4. [ ] Collect static files: `python manage.py collectstatic`
5. [ ] Run migrations: `python manage.py migrate`
6. [ ] Set secure `SECRET_KEY`
7. [ ] Configure HTTPS
8. [ ] Set up media file serving
9. [ ] Configure CORS if needed
10. [ ] Set up error logging

---

## 🔄 Maintenance Tasks

### Database Reset
```bash
rm db.sqlite3
python manage.py migrate
```

### Clear Static Cache
```bash
# Browser: Ctrl+Shift+R (hard refresh)
```

### Update Dependencies
```bash
pip install -r requirements.txt --upgrade
```

---

## 📞 Support

For issues or questions:
- Check PROJECT_STRUCTURE.md
- Review game/models.py for game logic
- Check browser console for JavaScript errors
- Review Django logs for backend errors

