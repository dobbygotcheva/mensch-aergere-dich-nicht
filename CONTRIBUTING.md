# Contributing to Mensch, ärgere dich nicht!

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

---

## 📋 Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Making Changes](#making-changes)
- [Submitting Pull Requests](#submitting-pull-requests)
- [Issue Reporting](#issue-reporting)

---

## 🤝 Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what's best for the community
- Show empathy towards other contributors

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Git
- Basic knowledge of Django
- Familiarity with HTML, CSS, JavaScript

### Fork and Clone
1. Fork the repository on GitHub
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/mensch-aergere-dich-nicht.git
   cd mensch-aergere-dich-nicht
   ```

---

## 💻 Development Setup

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Migrations
```bash
python manage.py migrate
```

### 4. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 5. Start Development Server
```bash
python manage.py runserver
```

---

## 📝 Coding Standards

Please follow the project's [CODE_STYLE_GUIDE.md](CODE_STYLE_GUIDE.md) for detailed guidelines.

### Quick Reference

#### Python
- Follow PEP 8
- Use 4 spaces for indentation
- Maximum line length: 120 characters
- Add docstrings to all functions and classes
- Use type hints where appropriate

```python
def function_name(param: str) -> bool:
    """
    Brief description.
    
    Args:
        param: Description
    
    Returns:
        Description
    """
    return True
```

#### JavaScript
- Use camelCase for variables/functions
- Use const/let (not var)
- Add semicolons
- Comment complex logic

```javascript
const functionName = (param) => {
    // Implementation
    return result;
};
```

#### HTML/CSS
- Use semantic HTML
- 2 spaces for indentation
- Follow BEM naming for CSS classes
- Ensure accessibility (alt tags, ARIA labels)

---

## 🔧 Making Changes

### Branch Naming
Create a descriptive branch name:
- `feature/add-multiplayer-support`
- `fix/dice-animation-bug`
- `docs/update-readme`
- `refactor/optimize-queries`

```bash
git checkout -b feature/your-feature-name
```

### Commit Messages
Write clear, descriptive commit messages:

```
feat: Add multiplayer support with WebSockets

- Implement Django Channels
- Add Redis for session management
- Update UI for real-time updates
```

Use prefixes:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Formatting, no code change
- `refactor:` Code restructuring
- `test:` Adding tests
- `chore:` Maintenance tasks

---

## 🎯 Areas for Contribution

### High Priority
- [ ] Unit tests for game logic
- [ ] Integration tests
- [ ] Mobile responsiveness improvements
- [ ] Accessibility enhancements
- [ ] Performance optimizations

### Medium Priority
- [ ] User authentication system
- [ ] Game statistics and leaderboards
- [ ] Sound effects
- [ ] Additional language translations
- [ ] AI opponents

### Nice to Have
- [ ] Tournament mode
- [ ] Custom game rules
- [ ] Additional themes
- [ ] Mobile app version

---

## 📤 Submitting Pull Requests

### Before Submitting

1. **Update your fork**
   ```bash
   git fetch upstream
   git merge upstream/main
   ```

2. **Test your changes**
   ```bash
   python manage.py test
   python manage.py runserver
   # Test manually in browser
   ```

3. **Check code quality**
   ```bash
   flake8 .
   black --check .
   ```

4. **Update documentation** if needed

### Pull Request Process

1. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request**
   - Go to GitHub
   - Click "New Pull Request"
   - Select your branch
   - Fill in the PR template

3. **PR Title Format**
   ```
   [Type] Brief description
   
   Example:
   [Feature] Add multiplayer support
   [Fix] Resolve dice animation bug
   [Docs] Update installation guide
   ```

4. **PR Description Should Include**
   - What changes were made
   - Why the changes were necessary
   - Any breaking changes
   - Screenshots (for UI changes)
   - Related issue numbers

### Example PR Description
```markdown
## Description
Adds support for real-time multiplayer using Django Channels.

## Changes
- Implemented WebSocket consumer for game state
- Added Redis for session management
- Updated UI to reflect real-time changes
- Added tests for multiplayer logic

## Testing
- Tested with 4 concurrent players
- Verified dice rolls synchronize
- Confirmed piece movements update for all players

## Screenshots
[Include screenshots here]

## Related Issues
Closes #123
```

---

## 🐛 Issue Reporting

### Before Creating an Issue
- Search existing issues to avoid duplicates
- Verify the issue exists in the latest version
- Collect relevant information

### Issue Template

**Bug Report:**
```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click on '...'
3. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
- OS: [e.g., Windows 10]
- Browser: [e.g., Chrome 90]
- Python version: [e.g., 3.9]
- Django version: [e.g., 4.2]

**Additional context**
Any other relevant information.
```

**Feature Request:**
```markdown
**Is your feature request related to a problem?**
A clear description of the problem.

**Describe the solution you'd like**
What you want to happen.

**Describe alternatives you've considered**
Other solutions you've thought about.

**Additional context**
Any other relevant information.
```

---

## 🧪 Testing Guidelines

### Writing Tests
```python
from django.test import TestCase
from game.models import Game, Player, Piece

class GameTestCase(TestCase):
    def setUp(self):
        self.game = Game.objects.create(status='in_progress')
    
    def test_game_creation(self):
        """Test that a game is created properly"""
        self.assertEqual(self.game.status, 'in_progress')
        self.assertEqual(self.game.current_player_index, 0)
```

### Running Tests
```bash
# Run all tests
python manage.py test

# Run specific test
python manage.py test game.tests.GameTestCase

# With coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

---

## 📚 Documentation

### Updating Documentation
- Keep README.md up to date
- Document all new features
- Update CONFIGURATION.md for new settings
- Add code comments for complex logic

### Documentation Structure
```
README.md           - Overview and quick start
PROJECT_STRUCTURE.md - Architecture details
CONFIGURATION.md    - Setup and customization
CODE_STYLE_GUIDE.md - Development standards
CONTRIBUTING.md     - This file
ENVIRONMENT.md      - Production deployment
```

---

## 🎨 Design Guidelines

### UI/UX Principles
- Maintain purple-pink gradient theme
- Use frosted glass effects consistently
- Ensure smooth animations (0.3s default)
- Keep responsive design in mind
- Test on multiple screen sizes

### Color Palette
- Gradient: `#667eea → #764ba2 → #f093fb`
- Text: `#fef3e2` (warm cream)
- Borders: `rgba(240, 147, 251, 0.4)` (pink)
- Backgrounds: `rgba(118, 75, 162, 0.3)` (purple)

---

## 📞 Getting Help

- 💬 **Discussions:** Use GitHub Discussions for questions
- 🐛 **Issues:** Report bugs via GitHub Issues
- 📧 **Email:** [contact email if applicable]
- 📖 **Docs:** Read the project documentation

---

## 🏆 Recognition

Contributors will be:
- Listed in project README
- Mentioned in release notes
- Credited in commit history
- Appreciated by the community! 🎉

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Mensch, ärgere dich nicht! 🎲✨

