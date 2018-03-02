# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 01:04:42 2018

@author: simet
"""
import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar, 
    QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
from networktables import NetworkTables 
import logging
logging.basicConfig(level=logging.DEBUG)


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.timer = QBasicTimer()
        self.step = 0
        self.timer.start(100, self)
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()
        
        
    def timerEvent(self, e):
        NetworkTables.initialize(server='10.61.62.2')
        sd = NetworkTables.getTable("SmartDashboard")
<<<<<<< HEAD
        content1=sd.getNumber('speed',0)
        content2=sd.getNumber('sw0',0)
        print(content1,content2)
=======
        content=sd.getNumber('Gyro',0)

        print(content)
>>>>>>> ec0aaff67f940aea48f816739c5896c62dea705d
        if self.step >= 100:
            self.timer.stop()
            return
            
        #self.step = self.step + 1
        
        self.pbar1.setValue(100*content/360)

        
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
    ex = Example()
    sys.exit(app.exec_())