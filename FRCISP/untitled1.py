# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 22:48:57 2018

@author: simet
"""

import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar, 
    QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
from networktables import NetworkTables 
import logging
logging.basicConfig(level=logging.DEBUG)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal,Qt
from PyQt5.QtGui import QPainter,QPen
import cv2

f=QFileDialog.getOpenFileNames(self,'打开','/','jpg')