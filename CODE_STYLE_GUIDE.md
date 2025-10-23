# Code Style Guide

## 📋 Table of Contents
1. [Python Style](#python-style)
2. [JavaScript Style](#javascript-style)
3. [HTML/Template Style](#htmltemplate-style)
4. [CSS Style](#css-style)
5. [File Organization](#file-organization)
6. [Naming Conventions](#naming-conventions)

---

## 🐍 Python Style

### General Guidelines
- Follow **PEP 8** style guide
- Use **4 spaces** for indentation
- Maximum line length: **120 characters**
- Use **snake_case** for variables and functions
- Use **PascalCase** for classes

### Imports
```python
# Standard library imports
from django.shortcuts import render, redirect

# Third-party imports
from django.contrib.auth.models import User

# Local imports
from .models import Game, Player
from .currency_mapping import CURRENCY_MAPPING
```

### Docstrings
```python
def function_name(param1, param2):
    """
    Brief description of what the function does.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    """
    pass
```

### Models
```python
class GameModel(models.Model):
    """
    Brief description of the model.
    """
    # Fields
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        """String representation"""
        return self.name
    
    def custom_method(self):
        """Description of custom method"""
        pass
```

### Views
```python
def view_name(request):
    """
    Description of what this view does.
    
    Args:
        request: HttpRequest object
    
    Returns:
        HttpResponse or JsonResponse
    """
    # Logic here
    return render(request, 'template.html', context)
```

---

## 💻 JavaScript Style

### General Guidelines
- Use **camelCase** for variables and functions
- Use **const** for constants, **let** for variables
- Use **arrow functions** where appropriate
- Add semicolons at end of statements

### Function Declaration
```javascript
// Use const for functions that won't be reassigned
const functionName = (param1, param2) => {
    // Function body
    return result;
};

// Or traditional function for callbacks
function handleEvent() {
    // Event handler
}
```

### AJAX Requests
```javascript
async function fetchData() {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json',
            }
        });
        
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
}
```

### Comments
```javascript
// Single-line comment for brief explanations

/**
 * Multi-line comment for detailed explanations
 * of complex logic or function purpose
 */
```

---

## 📄 HTML/Template Style

### Django Templates
```django
{% extends 'base.html' %}
{% load static %}

{% block title %}Page Title{% endblock %}

{% block extra_css %}
<style>
    /* Page-specific styles */
</style>
{% endblock %}

{% block content %}
    <div class="container">
        <!-- Content here -->
    </div>
{% endblock %}
```

### HTML Structure
- Use **semantic HTML** (header, nav, main, section, article, footer)
- Use **2 spaces** for indentation
- Close all tags properly
- Use lowercase for tag names and attributes

```html
<section class="game-section">
    <h2>Section Title</h2>
    <div class="content">
        <p>Content paragraph</p>
    </div>
</section>
```

### Accessibility
- Always include `alt` text for images
- Use proper heading hierarchy (h1, h2, h3)
- Include `aria-label` for icon buttons
- Ensure proper contrast ratios

```html
<img src="{% static 'images/dice1.png' %}" alt="Dice showing 1">
<button aria-label="Close modal" onclick="closeModal()">×</button>
```

---

## 🎨 CSS Style

### Organization
1. Layout properties (display, position, float)
2. Box model (width, height, margin, padding)
3. Typography (font, text properties)
4. Visual (color, background, border)
5. Misc (cursor, overflow, transitions)

### Example
```css
.element-class {
    /* Layout */
    display: flex;
    position: relative;
    
    /* Box model */
    width: 100%;
    padding: 1rem;
    margin: 0 auto;
    
    /* Typography */
    font-size: 1rem;
    font-weight: 600;
    text-align: center;
    
    /* Visual */
    color: #fef3e2;
    background: rgba(118, 75, 162, 0.3);
    border: 2px solid rgba(240, 147, 251, 0.4);
    border-radius: 12px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    
    /* Misc */
    transition: all 0.3s ease;
    cursor: pointer;
}
```

### Naming Convention (BEM-inspired)
```css
.block {}
.block__element {}
.block--modifier {}

/* Examples */
.player-card {}
.player-card__name {}
.player-card--active {}
```

### Color Variables
```css
:root {
    /* Player colors */
    --color-red: #ef5350;
    --color-blue: #42a5f5;
    
    /* Theme colors */
    --text-cream: #fef3e2;
    --bg-purple: rgba(118, 75, 162, 0.3);
    --border-pink: rgba(240, 147, 251, 0.4);
}
```

### Responsive Design
```css
/* Mobile first approach */
.element {
    width: 100%;
}

/* Tablet */
@media (min-width: 768px) {
    .element {
        width: 80%;
    }
}

/* Desktop */
@media (min-width: 1024px) {
    .element {
        width: 60%;
    }
}
```

---

## 📁 File Organization

### Python Files
```
module.py
├── Imports (grouped)
├── Constants
├── Helper functions
├── Main functions/classes
└── Utility functions
```

### JavaScript Files
```
script.js
├── Constants
├── State variables
├── Utility functions
├── Main functions
├── Event handlers
└── Initialize on load
```

### Template Files
```
template.html
├── {% extends %} and {% load %}
├── {% block title %}
├── {% block extra_css %} (if needed)
├── {% block content %}
└── {% block extra_js %} (if needed)
```

---

## 🏷️ Naming Conventions

### Python
```python
# Variables and functions
user_name = "John"
def calculate_total():
    pass

# Classes
class GameController:
    pass

# Constants
MAX_PLAYERS = 4
DEFAULT_COLOR = 'red'

# Private methods/variables
_internal_method()
_private_var = "value"
```

### JavaScript
```javascript
// Variables and functions
const playerName = "John";
function calculateTotal() {}

// Classes
class GameController {}

// Constants
const MAX_PLAYERS = 4;
const DEFAULT_COLOR = 'red';

// DOM elements
const btnRoll = document.getElementById('roll-button');
const playerCards = document.querySelectorAll('.player-card');
```

### CSS
```css
/* Components */
.player-card {}
.dice-section {}
.game-board {}

/* States */
.is-active {}
.is-disabled {}
.has-won {}

/* Utilities */
.text-center {}
.hidden {}
.fade-in {}
```

### Files
```
# Python modules
models.py
views.py
currency_mapping.py

# Templates
home.html
game_board.html
create_game.html

# Static files
style.css
game.js
dice1.png
```

---

## 📝 Comments Best Practices

### Python
```python
# TODO: Implement feature X
# FIXME: Bug in calculation
# NOTE: Important consideration
# HACK: Temporary workaround

def complex_function():
    """
    Detailed docstring explaining the function's purpose,
    parameters, and return values.
    """
    # Inline comment for complex logic
    result = complicated_calculation()
    return result
```

### JavaScript
```javascript
// TODO: Add error handling
// FIXME: Memory leak in animation
// NOTE: This relies on external API

/**
 * Detailed explanation of function
 * @param {number} value - The dice value
 * @returns {boolean} Whether move is valid
 */
function validateMove(value) {
    // Implementation
}
```

### CSS
```css
/* ==========================================================================
   Section Name
   ========================================================================== */

/* Component name
   ========================================================================== */

/* Sub-section comment */

/* Single line comment */
```

---

## ✅ Code Review Checklist

- [ ] Code follows style guidelines
- [ ] Functions have docstrings/comments
- [ ] Variable names are descriptive
- [ ] No hardcoded values (use constants)
- [ ] Error handling implemented
- [ ] No console.log() in production
- [ ] HTML is semantic and accessible
- [ ] CSS is organized and follows naming convention
- [ ] No duplicate code
- [ ] Code is DRY (Don't Repeat Yourself)

---

## 🔍 Linting Tools

### Python
```bash
# Install
pip install flake8 black pylint

# Run
flake8 .
black --check .
pylint game/
```

### JavaScript
```bash
# Install
npm install -g eslint

# Run
eslint static/js/
```

### CSS
```bash
# Install
npm install -g stylelint

# Run
stylelint "static/css/**/*.css"
```

---

## 📚 Additional Resources

- [PEP 8 - Python Style Guide](https://pep8.org/)
- [Django Coding Style](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)
- [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)
- [BEM Methodology](http://getbem.com/)
- [MDN Web Docs](https://developer.mozilla.org/)

---

*Last Updated: October 23, 2025*

