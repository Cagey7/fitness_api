from .base import *

SECRET_KEY = "django-insecure-1t=jt8q4(-oaud+=_+4kkp)tm6^em-i@s^9ms+caoeg5z%x9%("
ALLOWED_HOSTS = []
DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "fitness_api_development",
        "USER": "postgres",
        "PASSWORD": "123456",
        "HOST": "db",
        "PORT": "5432",
    }
}