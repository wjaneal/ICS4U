# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:19:43 2018

@author: simet
"""

"""
ZetCode PyQt5 tutorial 

In this example, a QCheckBox widget
is used to toggle the title of a window.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt
import sys
from networktables import NetworkTables 
import logging
logging.basicConfig(level=logging.DEBUG)
import time


# To see messages from networktables, you must setup logging




class Example(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.initUI()
    def executeSomething(self):
        '''
        NetworkTables.initialize(server='61.62.0.1')
        sd = NetworkTables.getTable("SmartDashboard")
        content='Power'+str(sd.getNumber('power','N/A'))
        print(content)
        cb = QCheckBox(content, self)
        cb.move(20, 20)
        cb.toggle()
        '''


        

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('power')
        self.show()
        
        
        
    def initUI(self):      
        '''
        if len(sys.argv) != 2:
            print("Error: specify an IP to connect to!")
            exit(0)
        '''
        time.sleep(1)
        print('test')
        '''
        while True:
            Example.executeSomething(self)
        '''




            
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())