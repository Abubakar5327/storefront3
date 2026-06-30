from storefront.settings.common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += [
    'silk',
]

# Add it to middleware locally
MIDDLEWARE += [
    'silk.middleware.SilkyMiddleware',
]
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hs6j037urx6iav+7#10%-vu4l4f5@@-1_zo)oft4g7$vf2$jmp'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront3',
        'HOST': 'mysql',
        'USER': 'root',
        'CONN_MAX_AGE': 60,
        'PASSWORD': '12345678'
    }
}

CELERY_BROKER_URL = 'redis://redis:6379/0'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        'TIMEOUT': 10 * 60, # 10 minutes
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

EMAIL_HOST = 'smtp4dev'
EMAIL_HOST_USER = ''
EMAILHOST_PASSWORD = ''
EMAIL_PORT = 2525 # '25'
DEFAULT_FROM_EMAIL = 'from@asdbuy.com'

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True,  # Always show the toolbar  
}