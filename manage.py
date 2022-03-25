#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import environ
import os
import sys
from core.settings.base import BASE_DIR
from django.core.management.commands.runserver import Command as runserver


env = environ.Env(
        # set casting, default value
        SECRET_KEY=str,
        RUN_SERVER_DEFAULT_PORT=str,
        DEBUG=(bool, False),
        TEMPLATE_DEBUG=(bool, False)
    )


def main():
    
    # Read environment variables from .env file
    environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
    
    """Run administrative tasks."""
    # Check env file for environment
    if env('ENV_NAME') == 'prod':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.prod')
    elif env('ENV_NAME') == 'staging':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.staging')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.dev')
    
    try:
        from django.core.management import execute_from_command_line
        
        # set default port
        runserver.default_port = env('RUN_SERVER_DEFAULT_PORT')
        
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
