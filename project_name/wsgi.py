"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

load_dotenv()

if os.environ['DEBUG'] == 'True':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{project_name}}.settings.local')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{project_name}}.settings.production')


application = get_wsgi_application()