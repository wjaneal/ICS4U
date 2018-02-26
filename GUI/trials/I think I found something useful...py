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

        self.pbar1 = QProgressBar(self)
        self.pbar1.setGeometry(30, 40, 200, 25)
        self.pbar2 = QProgressBar(self)
        self.pbar2.setGeometry(80, 100, 200, 25)
        self.timer = QBasicTimer()
        self.step = 0
        self.timer.start(100, self)
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()
        
        
    def timerEvent(self, e):
        NetworkTables.initialize(server='10.61.62.2')
        sd = NetworkTables.getTable("SmartDashboard")
        content1=sd.getNumber('Left',0)
        content2=sd.getNumber('Right',0)
        print(content1,content2)
        if self.step >= 100:
            self.timer.stop()
            return
            
        #self.step = self.step + 1
        
        self.pbar1.setValue(content1*100)
        self.pbar2.setValue(content2*100)
        
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