# Django settings for pgdayparis project.
import os

PROJECT_PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pgdayparis2016',  # Required to be non-empty string
        'USER': 'louisegrandjonc',  # Required to be non-empty string
    },
}

# Developpment database.
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME':'pgdayparis2016', # Required to be non-empty string
        'USER':'postgres', # Required to be non-empty string
        'PASSWORD':'postgres',
        'HOST':'localhost', # Set to empty string for localhost.
        'PORT':'', # Set to empty string for default.
    },
}

# Heroku database

import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = '/home/mha/djangolab/pgdayparis/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
#MEDIA_URL = '/media/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


# Static asset configuration
STATIC_ROOT = 'static'

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    './files/',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'zya5w8sfr)i(7q^p3750-3hk5&4=9(&z6+*1x!#lt#8h%!sizu'

# List of callables that know how to import templates from various sources.


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

WSGI_APPLICATION = 'pgdayparis.wsgi.application'

ROOT_URLCONF = 'pgdayparis.urls'

TEMPLATE_DIRS = (
    './templates',
)

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        'DIRS': {
            os.path.join(PROJECT_PATH, 'templates'),
        },
        "OPTIONS": {
            "match_extension": ('.html', ),
            'extensions': [
                "jinja2.ext.do",
                "jinja2.ext.loopcontrols",
                "jinja2.ext.with_",
                "jinja2.ext.i18n",
                "jinja2.ext.autoescape",

                "django_jinja.builtins.extensions.CsrfExtension",
                "django_jinja.builtins.extensions.CacheExtension",
                "django_jinja.builtins.extensions.TimezoneExtension",
                "django_jinja.builtins.extensions.UrlsExtension",
                "django_jinja.builtins.extensions.StaticFilesExtension",
                "django_jinja.builtins.extensions.DjangoFiltersExtension",
            ]
        }
    }
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'django_jinja',
    'pgdayparis',
    'pgdayparis.base',
)

DATETIME_FORMAT="Y-m-d H:i:s"
# If there is a local_settings.py, let it override our settings
try:
    from local_settings import *
except:
    pass


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

PGDAY_YEARS = [2015, 2016, 2017]

DEFAULT_YEAR = 2017
