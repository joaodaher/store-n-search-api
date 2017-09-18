import logging
import os
import sys

from envparse import env

logger = logging.getLogger(__name__)


# Paths
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Security
SECRET_KEY = env.str('SECRET_KEY', default='3.14159265359')
DEBUG = env.bool('DEBUG', default=True)
ALLOWED_HOSTS = []
USE_X_FORWARDED_HOST = True


# Logging
LOG_LEVEL = env.str('LOG_LEVEL', default='DEBUG' if DEBUG else 'INFO')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        },
        'sentry': {
            'level': LOG_LEVEL,
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': LOG_LEVEL,
            'propagate': True,
        },
        'root': {
            'level': LOG_LEVEL,
            'handlers': ['sentry'],
        },
        'raven': {
            'level': LOG_LEVEL,
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': LOG_LEVEL,
            'handlers': ['console'],
            'propagate': False,
        },
    },
}


SENTRY_DSN = env.str('SENTRY_DSN', default=None)
if SENTRY_DSN:
    RAVEN_CONFIG = {
        'dsn': SENTRY_DSN,
    }


# RestFul
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'PAGE_SIZE': env.int('PAGE_SIZE', default=50),
}


# Application
SITE_NAME = 'Store Search API'
SITE_URL = env.str('SITE_URL', default='http://local.store_search.com.br')
INSTALLED_APPS = [
    'raven.contrib.django.raven_compat',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'storages',
    'rest_framework',
    'v1.apps.V1Config',
]
ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'


# Internationalization
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Database
if 'SQL_HOST' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env.str('SQL_NAME', default='store_search_api'),
            'USER': env.str('SQL_USER', default='postgres'),
            'PASSWORD': env.str('SQL_PASSWORD', default=''),
            'HOST': env.str('SQL_HOST', default='localhost'),
            'PORT': env.str('SQL_PORT', default=''),
            'CONN_MAX_AGE': 60,
        }
    }
else:
    logger.warning("You're using a local file as database engine.")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'store_search_api.sqlite3'),
        }
    }


# Cache
if 'REDIS_HOST' in os.environ:
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": env.str('REDIS_HOST'),
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient"
            },
            "KEY_PREFIX": "store_search_api_"
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }
REST_FRAMEWORK_EXTENSIONS = {
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': env.int('CACHE_TTL', default=10),
    'DEFAULT_CACHE_ERRORS': False,
    'DEFAULT_CACHE_KEY_FUNC': 'utils.cache.cache_key_constructor',
}


# Middlewares
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# Templates & Static
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# AWS S3
AWS_ACCESS_KEY_ID = env.str('AWS_KEY', default=None)
AWS_SECRET_ACCESS_KEY = env.str('AWS_SECRET', default=None)
AWS_STORAGE_BUCKET_NAME = env.str('AWS_BUCKET', default=None)
AWS_S3_CUSTOM_DOMAIN = env.str('CDN_URL', default=None)
AWS_LOCATION = 'store_search_api'
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True
AWS_IS_GZIPPED = True

if AWS_STORAGE_BUCKET_NAME:
    DEFAULT_FILE_STORAGE = 'utils.aws.MediaRootS3BotoStorage'
    STATICFILES_STORAGE = 'utils.aws.StaticRootS3BotoStorage'
    S3_URL = '//{}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)
    MEDIA_URL = '//{}media/'.format(S3_URL)
    STATIC_URL = '//{}static/'.format(S3_URL)
    AWS_QUERYSTRING_AUTH = False
else:
    logger.warning("You're using a local storage for static and media files.")
    MEDIA_URL = MEDIA_ROOT + '/'
    STATIC_URL = STATIC_ROOT + '/'
