# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:12:43 2018

@author: simet
"""

import os

path = r"C:\Users\simet\Desktop\FRC"

def ui2py(path):
    uilist = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.ui')]
    pylist = [os.path.splitext(uifile)[0]+".py" for uifile in uilist]
    [os.system("pyuic5 -o {pyfile} {uifile}".format(pyfile=py, uifile=ui)) for py, ui in zip(pylist, uilist)]

if __name__ == "__main__":
    ui2py(path)