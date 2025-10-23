# 🎲 Mensch, ärgere dich nicht! (Don't Get Mad, Man!)

A beautiful Django-based web implementation of the classic German board game with a modern purple-pink themed UI and unique Bulgarian cultural elements.

![Game Status](https://img.shields.io/badge/status-active-success.svg)
![Django](https://img.shields.io/badge/django-4.2.11-green.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

---

## ✨ Features

### 🎮 Core Gameplay
- **Full game implementation** with authentic Ludo/Mensch ärgere dich nicht rules
- **4-player support** with turn-based gameplay
- **Piece capture mechanics** - send opponents back to start
- **Home lane completion** - first to get all 4 pieces home wins!
- **Dice rolling** with smooth animations
- **Real-time game state** updates

### 🎨 Visual Design
- **Purple-pink gradient theme** across all pages
- **Frosted glass UI elements** with backdrop blur effects
- **Smooth animations** and transitions
- **Team-specific character pieces** (Ninja Turtles, Philosophen, Musicians, Tigers)
- **Currency-themed board decorations** (Dollar, Euro, Leva, Roman coins)
- **Responsive layout** with optimized board size

### 🎯 Special Features
- **10 unique challenge tasks** distributed across the board
- **Bulgarian cultural themes** integrated into challenges
- **Modal popups** for interactive task display
- **Animated dice rolling** with image sequence
- **Game quit/resume** functionality
- **Multiple active games** support

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/mensch-aergere-dich-nicht.git
   cd mensch-aergere-dich-nicht
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start development server**
   ```bash
   python manage.py runserver
   ```

6. **Open in browser**
   ```
   http://localhost:8000
   ```

---

## 🎮 How to Play

1. **Start a new game** from the home page
2. **Enter player names** for all 4 players
3. **Roll the dice** on your turn
4. **Move your pieces** by clicking on highlighted pieces
5. **Complete challenges** when landing on special positions
6. **Capture opponents** by landing on their pieces
7. **Get all 4 pieces home** to win!

### Game Rules
- Roll **6** to get a piece out of start
- Complete **40 steps** on the main path before entering home
- Land on opponent pieces to **send them back to start**
- Exact roll needed for **final home position**

---

## 🏗️ Project Structure

```
mensch-aergere-dich-nicht/
├── dont_b_mad/              # Django project settings
├── game/                    # Main game application
│   ├── models.py           # Game, Player, Piece models
│   ├── views.py            # Game logic and API endpoints
│   ├── currency_mapping.py # Team/currency themes
│   └── special_tasks.py    # Challenge tasks
├── templates/              # HTML templates
│   ├── base.html          # Base layout
│   └── game/              # Game-specific templates
├── static/                 # Static assets
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript
│   └── images/            # Game images
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

For detailed architecture, see [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)

---

## 🎨 Teams & Themes

Each player represents a unique team with matching currency imagery:

| Team | Color | Currency | Characters |
|------|-------|----------|------------|
| 🐢 **Ninja Turtles** | Red | Dollar (USD) | Leonardo, Raphael, Donatello, Michelangelo |
| 🧠 **Philosophen** | Blue | Euro (EUR) | Hegel, Marx, Nietzsche, Schopenhauer |
| 🎵 **Musicians** | Green | Leva (BGN) | Beethoven, Liszt, Schumann, Todor Kolev |
| 🐯 **Tigers** | Yellow | Roman Coins | Bengal, Black, Siberian, White Tiger |

---

## 🎯 Special Challenges

Land on special positions to complete fun challenges:

- 📖 **Bai Ganio** - Bulgarian literature trivia
- 👠 **Catwalk** - Fashion model strut
- 💃 **Dance** - Show your moves!
- 🎶 **Burgas 63** - Sing Bulgarian hit song
- 💪 **Light Weight** - Quick workout
- 📚 **Dictionary** - Bulgarian language challenge
- 🌶️ **Hot Peppers** - Spicy food dare
- 🎵 **Music Break** - Play an instrument
- 🫁 **Luft Anhalten** - Hold your breath
- 🎤 **Radoi Ralin** - Poetry recitation

---

## 🛠️ Configuration

### Changing Colors
Edit theme colors in `templates/` or `static/css/style.css`:
```css
/* Main gradient */
background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);

/* Text color */
color: #fef3e2; /* Warm cream */

/* Borders */
border: 2px solid rgba(240, 147, 251, 0.4); /* Pink */
```

### Adding Teams
Edit `game/currency_mapping.py` to add or modify teams:
```python
CURRENCY_MAPPING = {
    'red': {
        'currency': 'dollar',
        'symbol': '$',
        'name': 'Your Team Name',
        # ... image paths
    }
}
```

### Adding Challenges
Edit `game/special_tasks.py` to add new challenges:
```python
SPECIAL_TASKS = {
    position_number: {
        'title': 'Challenge Title',
        'task': 'Challenge description',
        'type': 'challenge_type',
        'image': 'challenges/image.jpg'
    }
}
```

For complete configuration guide, see [CONFIGURATION.md](CONFIGURATION.md)

---

## 📚 Documentation

- **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** - Complete project architecture
- **[CONFIGURATION.md](CONFIGURATION.md)** - Configuration and customization guide
- **[CODE_STYLE_GUIDE.md](CODE_STYLE_GUIDE.md)** - Development guidelines and standards

---

## 🧪 Testing

```bash
# Run Django tests
python manage.py test

# Check for linting issues
flake8 .

# Format code
black .
```

---

## 🚀 Deployment

### Production Checklist

- [ ] Set `DEBUG = False` in `settings.py`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use environment variables for `SECRET_KEY`
- [ ] Set up production database (PostgreSQL)
- [ ] Configure static files serving
- [ ] Set up HTTPS/SSL
- [ ] Enable CSRF protection
- [ ] Configure logging

### Recommended Platforms
- **Heroku** - Easy deployment with free tier
- **PythonAnywhere** - Django-friendly hosting
- **DigitalOcean** - VPS with full control
- **AWS Elastic Beanstalk** - Scalable deployment

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please read [CODE_STYLE_GUIDE.md](CODE_STYLE_GUIDE.md) before contributing.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Original game: "Mensch, ärgere dich nicht!" by Josef Friedrich Schmidt
- Hardware project reference: Board position coordinates
- Currency images: Various sources
- Team character images: Various sources
- Challenge concepts: Bulgarian cultural traditions

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [documentation](PROJECT_STRUCTURE.md)
2. Review [configuration guide](CONFIGURATION.md)
3. Open an [issue](https://github.com/yourusername/mensch-aergere-dich-nicht/issues)

---

## 🎯 Roadmap

Future enhancements:
- [ ] Online multiplayer support
- [ ] User authentication
- [ ] Game statistics and leaderboards
- [ ] Mobile app version
- [ ] Additional language support
- [ ] Sound effects and music
- [ ] Tournament mode
- [ ] AI opponents

---

## 📸 Screenshots

### Home Page
Beautiful purple-pink gradient with animated elements and team showcases.

### Game Board
700px game board with currency decorations, team character pieces, and special challenge markers.

### Create Game
Elegant form with team information and smooth animations.

---

## 🏆 Credits

**Developed with ❤️ by the Mensch, ärgere dich nicht! Team**

⭐ Star this repo if you enjoyed it!

---

*Last updated: October 2025*
