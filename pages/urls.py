# -*- coding: utf-8 -*-
"""
URLs for pages.
"""
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from .views import page

urlpatterns = [
    url(r'^(?P<url>.*)$', page),
]

