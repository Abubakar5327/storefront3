import os
import dj_database_url
from storefront.settings.common import *

DEBUG = False

INSTALLED_APPS = [app for app in INSTALLED_APPS if app != 'debug_toolbar']
MIDDLEWARE = [m for m in MIDDLEWARE if 'debug_toolbar' not in m]

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['khaamat-bites-production.up.railway.app']


CSRF_VERIFICATION = ['khaamat-bites-production.up.railway.app']


import sys

DATABASE_URL = os.environ.get('DATABASE_URL')
if not DATABASE_URL:
    print("ERROR: DATABASE_URL environment variable is not set.", file=sys.stderr)
    sys.exit(1)

DATABASES = {
    'default': dj_database_url.config(
        env='DATABASE_URL',
        conn_max_age=600,
    )
}

REDIS_URL = os.environ.get('REDIS_URL', '')

CELERY_BROKER_URL = f"{REDIS_URL}/0"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"{REDIS_URL}/1",
        "TIMEOUT": 10 * 60,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

EMAIL_HOST = os.environ.get('MAILGUN_SMTP_SERVER', 'smtp.mailgun.org')
EMAIL_HOST_USER = os.environ.get('MAILGUN_SMTP_LOGIN', '')
EMAIL_HOST_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD', '')
EMAIL_PORT = int(os.environ.get('MAILGUN_SMTP_PORT', 2525))
EMAIL_USE_TLS = True