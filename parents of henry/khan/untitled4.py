# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 13:27:59 2018

@author: simet
"""
'''

def switch(one,another):
    c=one
    print(one,another)
    one=another
    print(one,another)
    another=c
    print(one,another)
a=1
b=2
switch(a,b)
print(a,b)'''
def switch(one,another):
    c=one
    print(one,another)
    one=another
    print(one,another)
    another=c
    print(one,another)
    return one,another
a=1
b=2
switch(a,b)
a=switch.one
b=switch.another
print(a,b)