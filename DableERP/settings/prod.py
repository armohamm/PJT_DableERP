from .common import *

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ['storages']

STATICFILES_STORAGE = 'transmedia.storages.StaticS3Boto3Storage'
DEFAULT_FILE_STORAGE = 'transmedia.storages.MediaS3Boto3Storage'

AWS_ACCESS_KEY_ID = 'xx'
AWS_SECRET_ACCESS_KEY = 'xx'
AWS_STORAGE_BUCKET_NAME = 'xx'
AWS_S3_REGION_NAME = 'ap-northeast-2'

import pymysql
pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'xx',
        'HOST': 'xx',
        'NAME': 'xx',
        'USER': 'xx',
        'PASSWORD': 'xx',
    }
}