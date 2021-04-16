import os

from conf.settings.base import ENV, ROOT_DIR

from conf.settings.initializers.database import *
from conf.settings.initializers.webpack import *
from conf.settings.initializers.logging import *
from conf.settings.initializers.admin_shortcuts import *


PROJECT_NAME = 'Hello World'
SECRET_KEY = ENV('SECRET_KEY')
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = os.path.join(ROOT_DIR, '_emails'),

EXTERNAL_APPS = [
    'django_extensions',
    'webpack_loader',
    'easy_thumbnails',
    'filer',
    'mptt',
]

PROJECT_APPS = [
    'apps.core',
    'apps.account.apps.AccountConfig', # Custom User Model
    'apps.web'
]
