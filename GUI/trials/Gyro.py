import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar, 
    QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
from networktables import NetworkTables 
import logging
logging.basicConfig(level=logging.DEBUG)
from PyQt5 import QtCore, QtGui, QtWidgets

class Example(QWidget):

    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):

        self.btn1 = QPushButton(self)
        self.btn1.setGeometry(130, 40, 200, 25)
        self.l1=QtWidgets.QLabel(self)
        self.l1.setGeometry(30,40,50,25)
        self.l1.setText('Left')
        
        self.btn2 = QPushButton(self)
        self.btn2.setGeometry(130, 75, 200, 25)
        self.l1=QtWidgets.QLabel(self)
        self.l1.setGeometry(30,75,50,25)
        self.l1.setText('Right')
        
        self.btn3 = QPushButton(self)
        self.btn3.setGeometry(130, 110, 200, 25)
        self.l1=QtWidgets.QLabel(self)
        self.l1.setGeometry(30,110,50,25)
        self.l1.setText('Camera')
        
        self.btn4 = QPushButton(self)
        self.btn4.setGeometry(130, 145, 200, 25)
        self.l1=QtWidgets.QLabel(self)
        self.l1.setGeometry(30,145,50,25)
        self.l1.setText('Gyro')
        
        
        
        
        self.timer = QBasicTimer()
        self.step = 0
        self.timer.start(100, self)
        self.setGeometry(300, 300, 400, 550)
        self.setWindowTitle('Input dialog')
        
        
        self.show()
    def timerEvent(self, e):
        NetworkTables.initialize(server='10.61.62.2')
        sd = NetworkTables.getTable("SmartDashboard")
        
        content1=str(sd.getNumber('left',0))
        print(content1)
        self.btn1.setText(content1)
        
        content2=str(sd.getNumber('right',0))
        print(content2)
        self.btn2.setText(content2)

        content3=str(sd.getNumber('camera',0))
        print(content3)
        self.btn3.setText(content3)

        content4=str(sd.getNumber('Gyro',0))
        print(content4)
        self.btn4.setText(content4)
        
        sd.putNumber('auto',1)



        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())