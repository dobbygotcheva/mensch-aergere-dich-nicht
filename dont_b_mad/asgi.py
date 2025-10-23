"""
ASGI config for dont_b_mad project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dont_b_mad.settings')

application = get_asgi_application()

