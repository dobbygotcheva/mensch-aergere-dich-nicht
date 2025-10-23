# Environment Configuration

## Development Setup

The project is currently configured for development with:
- `DEBUG = True`
- Development SECRET_KEY
- SQLite database

## Production Configuration

### Required Changes

#### 1. Secret Key
Change the SECRET_KEY in `dont_b_mad/settings.py`:
```python
import os
SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-key-here')
```

Generate a new secret key:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

#### 2. Debug Mode
```python
DEBUG = False
```

#### 3. Allowed Hosts
```python
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

#### 4. Database
Replace SQLite with PostgreSQL for production:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

#### 5. Static Files
```python
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
```

Run: `python manage.py collectstatic`

#### 6. Security Settings
Add to `settings.py`:
```python
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
```

## Environment Variables (Recommended)

Use environment variables for sensitive data:

```bash
# Linux/Mac
export SECRET_KEY='your-secret-key'
export DEBUG='False'
export DATABASE_URL='postgres://...'

# Windows
set SECRET_KEY=your-secret-key
set DEBUG=False
```

Or use a `.env` file with `python-decouple`:

```bash
pip install python-decouple
```

```python
# settings.py
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
```

## Heroku Deployment

```bash
# Install Heroku CLI
heroku create your-app-name

# Set environment variables
heroku config:set SECRET_KEY='your-secret-key'
heroku config:set DEBUG=False

# Add PostgreSQL
heroku addons:create heroku-postgresql:hobby-dev

# Deploy
git push heroku main

# Run migrations
heroku run python manage.py migrate
```

## Docker Deployment

Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "dont_b_mad.wsgi:application", "--bind", "0.0.0.0:8000"]
```

## Security Checklist

- [ ] SECRET_KEY is secure and not in version control
- [ ] DEBUG = False
- [ ] ALLOWED_HOSTS is properly configured
- [ ] Using PostgreSQL or similar production database
- [ ] Static files properly configured
- [ ] HTTPS/SSL enabled
- [ ] Security middleware enabled
- [ ] Regular backups configured
- [ ] Error logging configured

## Current Development Values

⚠️ **DO NOT USE IN PRODUCTION:**
- SECRET_KEY: `django-insecure-dev-key-change-this-in-production`
- DEBUG: `True`
- Database: SQLite (db.sqlite3)
- ALLOWED_HOSTS: `[]` (all hosts allowed in DEBUG mode)

