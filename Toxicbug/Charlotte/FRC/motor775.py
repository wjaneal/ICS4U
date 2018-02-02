#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 19:57:31 2018

@author: chenquancheng
"""
import math
#Option1
RPM=13675.856
torqueM=0.19116
m3=1.6
g=9.81
r3=0.6
m2=.5
r2=0.4
m1=1.5
r1=0.1
pi=4*math.atan(1)
gears=[3,5,7,10]
torqueRequired=0.5*m3*g*r3+m2*g*r2+m1*g*r1
print(torqueRequired)
speed=RPM/60*2*pi*0.02215
for i in gears:
    for j in gears:
        if torqueM*i*j>=1.2*torqueRequired:
            t=0.6/(speed/i/j)
            #if t<5:
            print("Torque:",torqueM*i*j,"speed:",speed/i/j,"Time",t,"Gears:",i,j)
'''
#Option2
m3=1.6
g=9.81
r3=0.6
m2=0.2
r2=0.4
m1=1
r1=0.3
pi=4*math.atan(1)
gears=[3,5,7,10]
torqueRequired=0.5*m3*g*r3+m2*g*r2+m1*g*r1
print(torqueRequired)
speed=RPM/60*2*pi*0.02215
for i in gears:
    for j in gears:
        if torqueM*i*j>=1*torqueRequired:
            t=0.6/(speed/i/j)
            #if t<5:
            print("Torque:",torqueM*i*j,"speed:",speed/i/j,"Time",t,"Gears:",i,j)
'''