# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'secret_key'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'path/to/database/file',
    }
}

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Google Maps API key
EASY_MAPS_GOOGLE_MAPS_API_KEY = 'google_maps_key'

# LDAP credentials
LDAP_URL = "blah"
LDAP_PORT = "389"
LDAP_ADMIN_OU = "blah"