"""
Django settings for sorted project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!!)!b*je#!!da*3ze%y^xcnm30bwi3k@qjx6!hhs$)vehme+l('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_auth',
    'bootstrapform',
    'bootstrap3',
    'tags',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.google.GoogleOAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.static',
)

ROOT_URLCONF = 'sorted.urls'

WSGI_APPLICATION = 'sorted.wsgi.application'

SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'
SOCIAL_AUTH_UID_LENGTH = 32
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 16
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 16

SOCIAL_AUTH_ENABLED_BACKENDS = ('google')

SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

GOOGLE_OAUTH2_CLIENT_ID      = '66555521259-uhs6g34ig49q8dsle1151qt86jq24nhl.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET  = 'xaU3Z28Kp57eIVMcXZMi1nAd'

LOGIN_URL          = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/login-error/'

SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'

SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS = ['iiitd.ac.in']



# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


STATIC_URL = '/static/'


STATICFILES_DIRS = ( 
    (os.path.join(PROJECT_ROOT, 'static')),
)

TEMPLATE_DIRS = ( 
	os.path.join(PROJECT_ROOT, 'templates'),
)

STATICFILES_FINDERS = {
 	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder'

}

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static/')


