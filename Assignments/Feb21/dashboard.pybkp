# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 01:04:42 2018

@author: simet
"""

from PyQt5.QtWidgets import (QWidget, QProgressBar, 
    QPushButton, QApplication,QLabel,QInputDialog,QLineEdit)
from PyQt5.QtCore import QBasicTimer
from networktables import NetworkTables 
import logging
logging.basicConfig(level=logging.DEBUG)
import sys
from networktables import NetworkTables

class DashBoard(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        #Progress Bar
        #self.pbar = QProgressBar(self)
        #self.pbar.setGeometry(30, 40, 200, 25)
        #self.timer = QBasicTimer()
        #self.step = 0
        #self.timer.start(100, self)
        self.setGeometry(500, 500, 600, 600)
        self.setWindowTitle('DashBoard')
        #speed
        self.speed_label = QLabel(self)
        self.speed_string="Speed"
        self.speed_label.setText (self.speed_string)
        self.speed_label.setGeometry(30,40,200,25)
        self.speed_value = QLabel(self)
        self.speed_value.setText('0')
        self.speed_value.setGeometry(100,40,200,25)
        #gyro
        self.gyro_label = QLabel(self)
        self.gyro_string="Gyro"
        self.gyro_label.setText(self.gyro_string)
        self.gyro_label.setGeometry(30,100,200,25)   
        #camera
        self.camera_label = QLabel(self)
        self.camera_string="Camera"
        self.camera_label.setText(self.camera_string)
        self.camera_label.setGeometry(30,160,200,25)
        self.camera_value = QLabel(self)
        self.camera_value.setText('Forward')
        self.camera_value.setGeometry(100,160,200,25)
        self.show()
        
        #Networktables
        #NetworkTables.initialize(server='10.61.62.2')
        #sd = NetworkTables.getTable("SmartDashboard")
        
        
    def timerEvent(self, e): 
        pass
'''
    def doAction(self):
      
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')
'''            
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    DB = DashBoard()
    sys.exit(app.exec_())