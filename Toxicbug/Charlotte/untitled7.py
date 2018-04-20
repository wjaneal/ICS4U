#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 13:49:44 2018

@author: miao
"""

def f(n):
    if n == 0:
        return 2
    if n >= 1:
        return f(n-1)*3 + 2