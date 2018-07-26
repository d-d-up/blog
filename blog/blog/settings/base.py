# coding: utf-8
from __future__ import absolute_import, unicode_literals
from os.path import join, abspath

from .settings import *


root = lambda *x: join(abspath(BASE_DIR), *x)

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-hans'

LOGIN_REDIRECT_URL = '/'

STATICFILES_DIRS = (
    root('static'),
)


INSTALLED_APPS += (
   'myblog',
)