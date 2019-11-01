import os

import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard.settings')
settings.DEBUG = False
django.setup()
