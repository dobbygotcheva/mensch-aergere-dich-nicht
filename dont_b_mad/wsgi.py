"""
WSGI config for dont_b_mad project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dont_b_mad.settings')

application = get_wsgi_application()

