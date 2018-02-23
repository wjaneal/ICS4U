#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 16:54:15 2018

@author: chenquancheng
"""
totalTime = 0
dataSet=[[-0.5,0,2,-1.0],[-0.3,0.4,1,1.0],[-0.5,0,5,-1.0]]
for i in dataSet:
    totalTime+=i[2]
intervals = 0
currentTime = 0
for i in range(0,len(dataSet)):
    dataSet[i].append([currentTime,currentTime+dataSet[i][2]])
    currentTime+=dataSet[i][2]
print(dataSet)