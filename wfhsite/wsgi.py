"""
WSGI config for wfhsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

python_env = os.getenv('PYTHON_ENV')
print('python_env=', python_env)

if python_env == 'production':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "wfhsite.settings.production")
elif python_env == 'test':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wfhsite.settings.dev")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wfhsite.settings.dev")
application = get_wsgi_application()
