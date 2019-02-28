"""
WSGI config for myapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#Development Settings per default 
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')

#Development or Production Settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings_.production')

application = get_wsgi_application()
