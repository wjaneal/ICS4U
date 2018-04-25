# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 17:45:16 2018

@author: 88660
"""
import os

path = r"C:\Users\simet\Documents\GitHub\ICS4U\GUI\translate"
def ui1py(path):
    pylist = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.py')]
    uilist = [os.path.splitext(pyfile)[0]+".ui" for pyfile in pylist]
    [os.system("pyuic5 -o {uifile} {pyfile}".format(uifile=ui, pyfile=py)) for ui, py in zip(uilist, pylist)]

def ui2py(path):
    uilist = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.ui')]
    pylist = [os.path.splitext(uifile)[0]+".py" for uifile in uilist]
    [os.system("pyuic5 -o {pyfile} {uifile}".format(pyfile=py, uifile=ui)) for py, ui in zip(pylist, uilist)]

if __name__ == "__main__":

    ui2py(path)
    
