#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 13:31:03 2018

@author: xuwentong
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

