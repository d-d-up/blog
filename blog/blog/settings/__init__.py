# coding: utf-8
from __future__ import absolute_import, unicode_literals
try:
    from .local import *
except ImportError:
    raise Exception('复制settings目录下的_local.py到local.py')