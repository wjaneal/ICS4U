# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 02:15:12 2018

@author: 11256
"""
''' 
(a)Name:Tony
(b)Date:January 16th
(c)Program title: quiz
(d)Purpose: make a quiz for people to answer the question and track the score
'''
D = {"What is the capital of China?":"Beijing","What is the largerst city in China?":"Hulun Buir","What is the capital city in Canada?":"Ottawa","What is the largerst city in Canada?":"Toronto","What is the capital city in America?":"Washington DC"}
Dk = list(D.keys())
Dv = list(D.values())
a=0
for i in range(0,len(D.keys())):
    answer0 = input(Dk[i])
    if answer0 == Dv[i]:
        a=a+1
        print ("You have", a, "score",)
    else:
        print ("You are wrong.")
        print ("You have", a, "score",)