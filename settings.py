# -*- coding: utf-8 -*-
import os

PROJECT_ROOT = os.path.dirname(__file__)
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
     ('ustas', 'ustas078@gmail.com'),
)

MANAGERS = ADMINS

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'pers.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''

    }
}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Kiev'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-Ru'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media_admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'inw2wpu8-+j+!135dcssd-fi8oq#aim+38c59223q37pmxv#fu'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
 #   'django.template.loaders.filesystem.load_template_source',
 #   'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "personal.context_processors.addsettings",
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'loginfo.middleware.MyMiddle',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
     os.path.join(PROJECT_ROOT, 'personal/templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'personal',
    'loginfo',
    'south',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/'

 # Exclude south on tests
if 'NOSE_WITH_DJANGO' in os.environ:
    INSTALLED_APPS = list(INSTALLED_APPS)
    INSTALLED_APPS.remove('south')
