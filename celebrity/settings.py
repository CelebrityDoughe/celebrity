"""
Django settings for celebrity project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j+@hwcy7n5y22z4i__%(q60c6&b3s0d7rpol+bmq#vhhv^6q%r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['celebritydbag.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'dynamic_scraper',
    'easy_thumbnails',
    'guardian',
    'social_auth',
    'south',
    'userena',

    'accounts',
    'news',
    'portals',
    'rating',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'celebrity.urls'

WSGI_APPLICATION = 'celebrity.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'celebrity_db',
        'USER': 'username',
        'PASSWORD': 'password'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/static/media/'
STATIC_ROOT = os.path.join(STATIC_ROOT, 'media')

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)


AUTHENTICATION_BACKENDS = (
    # normal email signin/signup
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',

    # facebook/twitter signin/signup
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.twitter.TwitterBackend',

    'django.contrib.auth.backends.ModelBackend',
)

ANONYMOUS_USER_ID = -1
SITE_ID = 1

AUTH_PROFILE_MODULE = 'accounts.UserProfile'

LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/login/success/'

# settings to be used for social login
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''

# this setting is changed because of social login with facebook
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'


USERENA_SIGNIN_AFTER_SIGNUP = True
USERENA_SIGNIN_REDIRECT_URL = '/'
USERENA_ACTIVATION_REQUIRED = False
USERENA_WITHOUT_USERNAMES = True


try:
    from local_settings import *  # noqa
except:
    pass
