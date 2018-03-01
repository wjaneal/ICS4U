#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Charlotte Chen
Date: Created on Wed Feb  7 13:15:00 2018
Title: Bubble Sort 
Purpose: Sort in ascending order using bubble sort an array of integers (length of n)
"""
import random
from heapq import merge

def bubbleSort(list1):
    for i in range(0,len(list1)-1):
        swapped=False
        for j in range(0,len(list1)-1-i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
                swapped=True
        if swapped==False:
            break
    return list1

def selectionSort(list1):
    for i in range(0,len(list1)-1):
        minIndex=i
        for j in range(i+1,len(list1)):
            if list1[j]<list1[minIndex]:
                minIndex=j
        if minIndex!=i:
            list1[i],list1[minIndex] = list1[minIndex],list1[i]
    return list1

def insertionSort(list1):
    for i in range(1,len(list1)):
        curNum=list1[i]
        for j in range(i-1,-1,-1):
            if list1[j]>curNum:
                list1[j+1]=list1[j]
            else:
                list1[j+1]=curNum
                break
        if list1[0]>curNum:
            list1[0]=curNum
    return list1

def mergeSort(list1):
    if len(list1) == 1:
        return list1
    middle=len(list1)//2
    L=list1[:middle]
    R=list1[middle:]
    L=mergeSort(L)
    R=mergeSort(R)
    return list(merge(L,R))
'''
def merge(a,b):
    c=[]
    while(len(a)>0 and len(b)>0):
        if a[0] > b[0]:
            c.append(b[0])
            b.remove(b[0])
        else:
            c.append(a[0])
            a.remove(a[0])
    while(len(a)>0):
        c.append(a[0])
    while(len(b)>0):
        c.append(b[0])
    return c
a=[]
b=[]
'''
list1=[]
for i in range(0,1000):
    list1.append(int(random.random()*1000))
print(bubbleSort(list1))
#print(selectionSort(list1))
#print(insertionSort(list1))
#print(mergeSort(list1))