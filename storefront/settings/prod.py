import os
import dj_database_url
from storefront.settings.common import *

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = [os.environ.get('RAILWAY_PUBLIC_DOMAIN', '')]

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