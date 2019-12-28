# -*- coding: utf-8 -*-
"""
URLs for pages.
"""
from __future__ import absolute_import, unicode_literals

from django.urls import path
from .views import page

urlpatterns = [
    path('<url>', page),
]

