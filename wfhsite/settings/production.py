from .base import *

DEBUG = False

SECRET_KEY = 'django-insecure-dyq2#b@cf=eo%9t0-j4^5$&0w!ms-8^v=e@=ha-l#q*btkh+!l'

ALLOWED_HOSTS = ['www.wfh.com', '127.0.0.1']
# ALLOWED_HOSTS = ['*']
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/3.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
