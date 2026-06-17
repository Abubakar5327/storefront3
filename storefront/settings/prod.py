from storefront.settings.common import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRET_KEY = os.environ.get['SECRET_KEY']

ALLOWED_HOSTS = []