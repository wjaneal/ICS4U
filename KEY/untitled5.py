#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:42:45 2017

@author: haichunkan
"""

from tkinter import *
from tkinter import messagebox
top = Tk()
C = Canvas(top, bg="white", height=300, width=300)
m=input("m=") 
b=input("b=")
linedraw=C.create_line(10,10*m+b,290,290*m+b,fill="black")
C.pack
top.mainloop()
     