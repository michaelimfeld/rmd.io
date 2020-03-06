import os
import datetime

import environ

env = environ.Env()
django_root = environ.Path(__file__) - 2
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Database definition
DATABASES = {
    "default": {
        "ENGINE": env.str(
            "DJANGO_DATABASE_ENGINE", default="django.db.backends.postgresql_psycopg2"
        ),
        "NAME": env.str("DJANGO_DATABASE_NAME", default="rmdio"),
        "USER": env.str("DJANGO_DATABASE_USER", default="rmdio"),
        "PASSWORD": env.str("DJANGO_DATABASE_PASSWORD", default="rmdio"),
        "HOST": env.str("DJANGO_DATABASE_HOST", default="localhost"),
        "PORT": env.str("DJANGO_DATABASE_PORT", default="5432"),
    }
}

# Application definition
DEBUG = env.bool("DJANGO_DEBUG", default=False)
SECRET_KEY = env.str("DJANGO_SECRET_KEY", default="uuuuuuuuuu")
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["*"])
HOST_PROTOCOL = env.str("DJANGO_HOST_PROTOCOL", default="http")
HOST_DOMAIN = env.str("DJANGO_HOST_DOMAIN", default="localhost:4200")

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django_extensions',
    'mails',
    'widget_tweaks',
]
MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'maildelay.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
          os.path.join(BASE_DIR, 'templates')
        ],
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
WSGI_APPLICATION = 'maildelay.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/
TIME_ZONE = 'Europe/Zurich'
LANGUAGE_CODE = 'en-us'
SITE_URL = env.str("DJANGO_SITE_URL", default="http://localhost")
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = '/var/www//app/app/static'
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Login redirects to
LOGIN_REDIRECT_URL = '/mails/'
LOGIN_REDIRECT_URL_FAILURE = '/login/'
LOGOUT_REDIRECT_URL = '/home/'

# Auth
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'mails.auth.EmailBackend'
]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Media
MEDIA_ROOT = ''
MEDIA_URL = ''

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ("[%(asctime)s] %(levelname)s "
                       "[%(name)s:%(lineno)s] %(message)s"),
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, "error.log"),
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'mails': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

# Mailserver login settings
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", default="maildelay@dev.rmd.io")
DEFAULT_FROM_EMAIL = env.str("EMAIL_FROM_USER", default="maildelay@dev.rmd.io")
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", default="rmdio")
EMAIL_HOST = env.str("EMAIL_HOST", default="localhost")
EMAIL_FOLDER = 'INBOX'

MAILBOXES = [
    ('1d', 'Mail Delay for 1 day'),
    ('2d', 'Mail Delay for 2 days'),
    ('3d', 'Mail Delay for 3 days'),
    ('4d', 'Mail Delay for 4 days'),
    ('5d', 'Mail Delay for 5 days'),
    ('6d', 'Mail Delay for 6 days'),
    ('7d', 'Mail Delay for 7 days'),
    ('8d', 'Mail Delay for 8 days'),
    ('9d', 'Mail Delay for 9 days'),
    ('10d', 'Mail Delay for 10 days'),
    ('11d', 'Mail Delay for 11 days'),
    ('1w', 'Mail Delay for 1 week'),
    ('2w', 'Mail Delay for 2 weeks'),
    ('3w', 'Mail Delay for 3 weeks'),
    ('4w', 'Mail Delay for 4 weeks'),
    ('5w', 'Mail Delay for 5 weeks'),
    ('6w', 'Mail Delay for 6 weeks'),
    ('7w', 'Mail Delay for 7 weeks'),
    ('8w', 'Mail Delay for 8 weeks'),
    ('9w', 'Mail Delay for 9 weeks'),
    ('10w', 'Mail Delay for 10 weeks'),
    ('11w', 'Mail Delay for 11 weeks'),
    ('1m', 'Mail Delay for 1 month'),
    ('2m', 'Mail Delay for 2 months'),
    ('3m', 'Mail Delay for 3 months'),
    ('4m', 'Mail Delay for 4 months'),
    ('5m', 'Mail Delay for 5 months'),
    ('6m', 'Mail Delay for 6 months'),
    ('7m', 'Mail Delay for 7 months'),
    ('8m', 'Mail Delay for 8 months'),
    ('9m', 'Mail Delay for 9 months'),
    ('10m', 'Mail Delay for 10 months'),
    ('11m', 'Mail Delay for 11 months'),
]

BLOCK_DELAYS = {
    1: datetime.timedelta(minutes=10),
    2: datetime.timedelta(hours=1),
    3: datetime.timedelta(days=1),
    4: datetime.timedelta(days=3),
    5: datetime.timedelta(days=7)
}

EMAIL_SUFFIX_TO_DAY = {
    'd': 1,
    'w': 7,
    'm': 30,
}


CALENDAR_STRIP_PREFIXES = (
    r'^Re:\s*',
    r'^Ant:\s*',
    r'^Fwd:\s*',
    r'^Wg:\s*',
)
