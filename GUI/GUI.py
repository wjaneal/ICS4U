#IUOYTMK
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
        self.motor1 = QProgressBar(self)
        self.motor1.setGeometry(150,100,100,200)
        self.motor1.setValue(0)
        
        self.motor2 = QProgressBar(self)
        self.motor2.setGeometry(150,320,100,200)
        self.motor2.setValue(0)
        
        self.motor3 = QProgressBar(self)
        self.motor3.setGeometry(250,100,100,200)
        self.motor3.setValue(0)
        
        self.motor4 = QProgressBar(self)
        self.motor4.setGeometry(250,320,100,200)
        self.motor4.setValue(0)
        
        self.elv1 = QPushButton(self)
        self.elv1.setGeometry(500,100,50,50)
        
        self.elv2 = QPushButton(self)
        self.elv2.setGeometry(600,100,50,50)
        
        self.Left = QPushButton(self)
        self.Left.setGeometry(150,20,50,50)
        self.Left.setText('L')
        
        self.Right = QPushButton(self)
        self.Right.setGeometry(250,20,50,50)
        self.Right.setText('R')
        
        self.dist = QPushButton(self)
        self.dist.setGeometry(20,370,100,50)
        self.dist.setText('Distance')
        
        self.time = QPushButton(self)
        self.time.setGeometry(340,370,100,50)
        self.time.setText('Time')
        
        self.dist1 = QPushButton(self)
        self.dist1.setGeometry(140,370,100,50)
        self.dist2 = QPushButton(self)
        self.dist2.setGeometry(140,450,100,50)
        self.time1 = QPushButton(self)
        self.time1.setGeometry(4)
        
        
        self.auto1 = QPushButton(self)
        self.auto2 = QPushButton(self)
        self.auto3 = QPushButton(self)
        self.auto4 = QPushButton(self)
        self.auto5 = QPushButton(self)
        self.auto6 = QPushButton(self)
        self.auto7 = QPushButton(self)
        self.auto8 = QPushButton(self)
        self.auto9 = QPushButton(self)
        self.auto10 = QPushButton(self)
        self.auto11 = QPushButton(self)
        self.auto12 = QPushButton(self)
        self.Tobe = QPushButton(self)
        self.driNum = QPushButton(self)
        
        self.gyro = QtWidgets.QLabel(self)
        self.arm = QtWidgets.QLabel(self)
        self.auto = QtWidgets.QLabel(self)
        self.Automata = QtWidgets.QLabel(self)
        self.driFac= QtWidgets.QLabel(self)
        
        
        '''
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
        
        self.atbt1 = QPushButton(self)
        self.atbt1.setGeometry(30,180,50,25)
        self.atbt1.setText('1')
        self.atbt1.clicked.connect(self.changeat1)
        
        self.atbt1 = QPushButton(self)
        self.atbt1.setGeometry(90,180,50,25)
        self.atbt1.setText('2')
        self.atbt1.clicked.connect(self.changeat2)
        
        self.atbt1 = QPushButton(self)
        self.atbt1.setGeometry(150,180,50,25)
        self.atbt1.setText('3')
        self.atbt1.clicked.connect(self.changeat3)
        
        self.atbt1 = QPushButton(self)
        self.atbt1.setGeometry(210,180,50,25)
        self.atbt1.setText('4')
        self.atbt1.clicked.connect(self.changeat4)

                
        self.timer = QBasicTimer()
        self.step = 0
        self.timer.start(100, self)
        '''
        self.setGeometry(100, 100, 1500, 900)
        self.setWindowTitle('Input dialog')
        
        
        self.show()
        
        
    def timerEvent(self, e):
        '''
        NetworkTables.initialize(server='10.61.62.2')
        self.sd = NetworkTables.getTable("SmartDashboard")
        
        content1=str(self.sd.getNumber('left',0))
        #print(content1)
        self.btn1.setText(content1)
        
        content2=str(self.sd.getNumber('right',0))
        #print(content2)
        self.btn2.setText(content2)

        content3=str(self.sd.getNumber('camera',0))
        #print(content3)
        self.btn3.setText(content3)

        content4=str(self.sd.getNumber('Gyro',0))
        #print(content4)
        self.btn4.setText(content4)
        
    def changeat1(self):
        print('clicked')
        self.sd.putNumber('auto',1)
    def changeat2(self):
        print('clicked')
        self.sd.putNumber('auto',2)
    def changeat3(self):
        print('clicked')
        self.sd.putNumber('auto',3)
    def changeat4(self):
        print('clicked')
        self.sd.putNumber('auto',4)
'''


        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
