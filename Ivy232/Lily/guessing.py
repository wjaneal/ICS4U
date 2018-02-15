#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:38:53 2018

@author: user
"""

import random
list4 = random.randint(0,100)
while True:
    number = input("")
    if int(number) > list4:
        print("Too high")
    elif int(number) < list4:
        print("Too low")
    else:
        print("Just right!")
        break
    