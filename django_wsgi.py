#!/usr/bin/env python
# coding:utf-8
__author__ = 'Stone'
__date__ = '2018/05/13'

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'redis_admin.settings'
import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()