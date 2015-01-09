from django.conf import global_settings
"""
Django settings for DrScratch project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATIC_URL = '/resources/'

STATICFILES_DIRS = (
os.path.join(BASE_DIR, 'resources'),
)

STATIC_ROOT = '/resources/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b&0vhl+ghtc+31i7xmq@$t)n^)*8p3a9!p8=pk2z9tb5om*(&l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



FILE_UPLOAD_HANDLERS = ('django.conf.UploadProgressCachedHandler.UploadProgressCachedHandler', ) + \
    global_settings.FILE_UPLOAD_HANDLERS


TEMPLATE_DEBUG = True

TEMPLATE_LOADERS = (
'django.template.loaders.filesystem.Loader',
'django.template.loaders.app_directories.Loader',
#'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = ('templates',)

ALLOWED_HOSTS = ['localhost', '193.147.51.252','drscratchpre.programamos.es']


# Application definition

INSTALLED_APPS = (
    'DrScratchApp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'DrScratch.urls'

WSGI_APPLICATION = 'DrScratch.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = 'resources'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/resources/'
