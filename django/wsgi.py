"""
WSGI config for web_pnp_report project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

path = os.path.dirname(__file__)

if path not in sys.path:
    sys.path.append(path)

os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_pnp_report.settings')

application = get_wsgi_application()
