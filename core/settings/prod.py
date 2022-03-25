from .base import *


DEBUG = env('DEBUG')

TEMPLATE_DEBUG = env('DEBUG') 

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': env('DATABASE_ENGINE'),
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PW'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}