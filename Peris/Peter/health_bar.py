# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 12:52:07 2018

@author: 84999
"""

def health_bar(self,Bn,Nm,Ba):
        self.Bnhp = 200
        self.Nmhp = 100
        self.Bahp = 500
        self.Bn = input("what does Baron do?")
        if self.Bn == ("fight","attack", "slice", "hack", "destroy"):
            print("Baron use physical attack!")
            self.Nmhp-50
            self.Bahp-250
        if self.Nmhp == 0:
            print("you defeated the nightmare!!")
        if self.Bahp == 0:
            print("youd defeated the bloody ape!!")
            
        