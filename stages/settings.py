"""
Django settings for stages project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from stages.settings_local import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Config pour Django-cas-ng
CAS_SERVER_URL = "https://login.telecom-bretagne.eu/cas/"
CAS_CREATE_USER = False

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'django_cas_ng.backends.CASBackend',
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# Config pour l'envoi de mails
SERVER_EMAIL = 'stages-bot@resel.fr'
EMAIL_USE_TLS = True
EMAIL_HOST = 'pegase.adm.resel.fr'
EMAIL_SUBJECT_PREFIX = ''

ADMINS = [
    ('ML de stages', 'stages-admin@resel.fr'),
]

ALLOWED_HOSTS = ['stages.resel.fr', 'localhost']

# Pour le login et logout
LOGIN_URL = '/login'
LOGOUT_URL = '/logout'
LOGIN_REDIRECT_URL = '/'

# Expiration de session pour les users connectés
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

DEFAULT_CHARSET = 'utf-8'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'easy_maps',
    'django_cas_ng',
    'pages',
    'post',
    'search',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'stages.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), '/var/www/stages/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'pages.context_processors.mobile',
            ],
        },
    },
]

WSGI_APPLICATION = 'stages.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "sfiles"),
)

# Media files (upload d'annonces au format .pdf ou .txt)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s [%(levelname)s] %(module)s %(process)d %(thread)d : %(message)s'
        },
        'simple': {
            'format': '%(asctime)s [%(levelname)s] %(module)s : %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/srv/www/stages.resel.fr/logs/debug.log',
            'formatter': 'simple',
            'encoding': 'utf8',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'verbose',
            'include_html': True,
        },
        'logstash': {
            'level': 'DEBUG',
            'class': 'logstash.LogstashHandler',
            'host': 'orion.adm.resel.fr',
            'port': 5959,  # Default value: 5959
            'version': 1,
            'message_type': 'django',
            'fqdn': False,  # Fully qualified domain name. Default value: false.
            'tags': None,  # list of tags. Default: None.
        },
    },
    'loggers': {
        'default': {
            'handlers': ['file', 'logstash'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers': ['file', 'logstash'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
