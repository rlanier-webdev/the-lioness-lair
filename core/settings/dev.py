from .base import *

DEBUG = env('DEBUG')

TEMPLATE_DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']

# DEV DB SETTINGS 
DATABASES = {
    'default': {
        'ENGINE': env('DATABASE_ENGINE'),
        'NAME': BASE_DIR / env('DATABASE_NAME'),
    }
}