from settings.base import *


# Database
if 'TRAVIS' in os.environ:
    logger.warning("You're actually using Travis's database service.")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'travisci',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

# Cache
if 'REDIS_HOST' not in os.environ:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'unique-snowflake',
            'OPTIONS': {
                'CLIENT_CLASS': 'utils.cache.CacheClient',
            }
        }
    }
