
'''
Name:Khan
Date: April 9, 2018
Title: GUI for robot
propose:(1) Display necessary information for drivers to control the robot.
        (2) Allow the drivers to choose autonomous type for the robot
variables: VideoSignal,cap,run_video,self.ip,height,width, motor1,motor2,motor3,motor4,elv1,Elv1,elv2,Left,Right,dist,time,dist1,time1,auto1,auto2,auto3,auto4,auto5,auto6,auto7,auto8,auto9,ToBe,driNum,Gyro,ArmState,arm,AutoMATA,driFac,timer,step,NetworkTables,M0,M1,M2,M3,E0,E1,D1,D2,T1,T2,G1
'''
import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar, 
    QPushButton, QApplication,QTextEdit,QFileDialog)
from PyQt5.QtCore import QBasicTimer
from networktables import NetworkTables 
import logging
logging.basicConfig(level=logging.DEBUG)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal,Qt
from PyQt5.QtGui import QPainter,QPen
import cv2
#This is to import the modules
class ShowVideo(QtCore.QObject):
 
    
    VideoSignal = QtCore.pyqtSignal(QtGui.QImage)#This is to get the signal
    
 
    def __init__(self, parent = None):
        super(ShowVideo, self).__init__(parent)
        self.ip='10.61.62.20:8081'#This is to initialize the vedio player and get the ip
    @QtCore.pyqtSlot()
    def startVideo(self):
        run_video = True#This is to start the the player
        while run_video:
            self.cap = cv2.VideoCapture("http://"+ str(self.ip)+":8081/?action=stream?dummy=param.mjpg")
            #This is to get the image
            ret, image = self.cap.read()
            #This is to read the image
            color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            #This is to convert the image into signal
            height, width, _ = color_swapped_image.shape
            qt_image = QtGui.QImage(color_swapped_image.data,
                                    width,
                                    height,
                                    color_swapped_image.strides[0],
                                    QtGui.QImage.Format_RGB888)
 
            self.VideoSignal.emit(qt_image)#This is to send out the signal
class GUI(QWidget):

    def __init__(self,parent = None):
        super().__init__()
        self.ip='10.61.62.3'
        #This is to initialize the gui
        self.initUI()
        #self.cap = cv2.VideoCapture("http://"+ str(self.ip) +":8081/?action=stream?dummy=param.mjpg")
        self.CAM_NUM = 0
        super(GUI, self).__init__(parent)
        self.image = QtGui.QImage()#This is to set up the image
        self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)
    def paintEvent(self, event):#This is to show the image
        painter = QtGui.QPainter(self)
        painter.drawImage(0,0, self.image)
        self.image = QtGui.QImage()
        '''
        qp=QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()
        '''
    def setImage(self, image):
        if image.isNull():#This is when there is no image
            print("Viewer Dropped frame!")
 
        self.image = image
        if image.size() != self.size():
            self.setFixedSize(image.size())#This is to show the image
        self.update()
        '''
    def drawLines(self,qp):
        pen=QPen(Qt.black,2,Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(200,400,1500,400)
        print("i drawed but there is no lines")
        '''
        
    def initUI(self):#This is to set up some widgets
        #This is to display the motors
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
        #This is to display the elvator motors
        self.elv1 = QPushButton(self)
        self.elv1.setGeometry(500,100,50,50)
        self.Elv1=QtWidgets.QLabel(self)
        self.Elv1.setGeometry(500,150,200,50)
        self.Elv1.setText('Elevators')
        
        
        self.elv2 = QPushButton(self)
        self.elv2.setGeometry(600,100,50,50)
        #This is to  mark the position
        self.Left = QPushButton(self)
        self.Left.setGeometry(150,20,50,50)
        self.Left.setText('L')
        
        self.Right = QPushButton(self)
        self.Right.setGeometry(250,20,50,50)
        self.Right.setText('R')
        #This is to mark the distance
        self.dist = QPushButton(self)
        self.dist.setGeometry(20,670,100,50)
        self.dist.setText('Distance:')
        #This is to mark the time
        self.time = QPushButton(self)
        self.time.setGeometry(340,670,100,50)
        self.time.setText('Time:')
        #This is to display the distance and time
        self.dist1 = QPushButton(self)
        self.dist1.setGeometry(140,670,100,50)
        self.dist2 = QPushButton(self)
        self.dist2.setGeometry(140,750,100,50)
        
        self.time1 = QPushButton(self)
        self.time1.setGeometry(460,670,100,50)
        self.time2 = QPushButton(self)
        self.time2.setGeometry(460,750,100,50)
        
        
        #This is to set up the autonomous buttons
        self.auto1 = QPushButton(self)
        self.auto1.setGeometry(600,670,40,40)
        self.auto1.setText('1')
        self.auto1.clicked.connect(self.A1)        
        self.auto2 = QPushButton(self)
        self.auto2.setGeometry(640,670,40,40)
        self.auto2.clicked.connect(self.A2)
        self.auto2.setText('2')
        self.auto3 = QPushButton(self)
        self.auto3.setGeometry(680,670,40,40)
        self.auto3.setText('3')
        self.auto3.clicked.connect(self.A3)
        self.auto4 = QPushButton(self)
        self.auto4.setGeometry(720,670,40,40)
        self.auto4.setText('4')
        self.auto4.clicked.connect(self.A4)
        self.auto5 = QPushButton(self)
        self.auto5.setGeometry(760,670,40,40)
        self.auto5.setText('5')
        self.auto5.clicked.connect(self.A5)
        self.auto6 = QPushButton(self)
        self.auto6.setGeometry(800,670,40,40)
        self.auto6.setText('6')
        self.auto6.clicked.connect(self.A6)
        self.auto7 = QPushButton(self)
        self.auto7.setGeometry(840,670,40,40)
        self.auto7.setText('7')
        self.auto7.clicked.connect(self.A7)
        self.auto8 = QPushButton(self)
        self.auto8.setGeometry(880,670,40,40)
        self.auto8.setText('8')
        self.auto8.clicked.connect(self.A8)
        self.auto9 = QPushButton(self)
        self.auto9.setGeometry(920,670,40,40)
        self.auto9.setText('9')
        self.auto9.clicked.connect(self.A9)
        #This is to show the currently used autonomous code
        self.ToBe = QPushButton(self)
        self.ToBe.setGeometry(800,750,100,50)
        self.ToBe.setText('not running')
        #This is to show the drive number
        self.driNum = QPushButton(self)
        self.driNum.setGeometry(800,250,50,50)
        #This is to show the gyro
        self.Gyro=QPushButton(self)
        self.Gyro.setGeometry(900,250,50,50)
        self.Gyro.setText('0')
        #This is to show the arm movement state index
        self.ArmState=QPushButton(self)
        self.ArmState.setGeometry(1000,250,200,50)
        self.ArmState.setText('not sure')
        #This is to label the variables
        self.gyro = QtWidgets.QLabel(self)
        self.gyro.setGeometry(900,170,100,50)
        self.gyro.setText('gyro:')
        self.arm = QtWidgets.QLabel(self)
        self.arm.setGeometry(1000,170,100,50)
        self.arm.setText('arm:')
        self.AutoMATA = QtWidgets.QLabel(self)
        self.AutoMATA.setGeometry(600,750,250,50)
        self.AutoMATA.setText('Current autonomous code:')
        self.driFac= QtWidgets.QLabel(self)
        self.driFac.setGeometry(800,170,200,50)
        self.driFac.setText('driver factor:')
        #choose and show the intruction document
        self.tx=QTextEdit(self)
        self.tx.setGeometry(400,300,500,300)
        self.stx=QPushButton('select document',self)
        self.stx.setGeometry(450,250,100,50)
        self.stx.clicked.connect(self.openfile)
        #This is to start the timer event
        self.timer = QBasicTimer()
        self.step = 0
        self.timer.start(100, self)
        
        self.setGeometry(100, 100, 1500, 900)
        self.setWindowTitle('Input dialog')
        
        
        self.show()
    def openfile(self):#open a text file
        fname = QFileDialog.getOpenFileName(self,'open file','./')#get the file name
        if fname[0]:
            with open(fname[0],'r',encoding='gb18030',errors='ignore') as f:#detect whether it is a text file?not sure
                self.tx.setText(f.read())
        #this seems to be working but the text box just shows random charaters....?????????????????
        #why????????????????????????????????????????????????????????????????????????????????
        
    def timerEvent(self, e):
        #This is to put the numbers into networkktable
        '''
        NetworkTables.initialize(server='10.61.62.2')#Initializing
        '''
        self.sd = NetworkTables.getTable("SmartDashboard")
        #Display motor values        
        M0 = self.sd.getNumber('M0',0)
        self.motor1.setValue(M0*100)
        M1 = self.sd.getNumber('M1',0)
        self.motor2.setValue(M1*100)
        M2 = self.sd.getNumber('M2',0)
        self.motor3.setValue(M2*100)
        M3 = self.sd.getNumber('M3',0)
        self.motor4.setValue(M3*100)
        E0 = self.sd.getNumber('E0',0)
        self.elv1.setText(str(E0))
        E1 = self.sd.getNumber('E1',0)
        self.elv2.setText(str(E1))
        #Show encoder values
        D1= self.sd.getNumber('EC1',0)
        self.dist1.setText(str(D1))
        D2= self.sd.getNumber('EC2',0)
        self.dist2.setText(str(D2))
        T1= self.sd.getNumber('EC3',0)
        self.time1.setText(str(T1))
        T2= self.sd.getNumber('EC4',0)
        self.time2.setText(str(T2))
        G1= self.sd.getNumber('gyro',0)
        self.Gyro.setText(str(G1))
    #This is to def the autonomous buttons' functions
    def A1(self):
        print('clicked')
        self.sd.putNumber('auto',1)
        self.ToBe.setText('1')
    def A2(self):
        print('clicked')
        self.sd.putNumber('auto',2)
        self.ToBe.setText('2')
    def A3(self):
        print('clicked')
        self.sd.putNumber('auto',3)
        self.ToBe.setText('3')
    def A4(self):
        print('clicked')
        self.sd.putNumber('auto',4)
        self.ToBe.setText('4')
    def A5(self):
        print('clicked')
        self.sd.putNumber('auto',5)
        self.ToBe.setText('5')
    def A6(self):
        print('clicked')
        self.sd.putNumber('auto',6)
        self.ToBe.setText('6')
    def A7(self):
        print('clicked')
        self.sd.putNumber('auto',7)
        self.ToBe.setText('7')
    def A8(self):
        print('clicked')
        self.sd.putNumber('auto',8)
        self.ToBe.setText('8')
    def A9(self):
        print('clicked')
        self.sd.putNumber('auto',9)
        self.ToBe.setText('9')

    #This is to show the whole thing
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    #this is to put an image of our robot in to the gui
    
    #however, the filename seems to be in wrong format
    
    #w=QtWidgets.QWidget()
    #photo=QtWidgets.QLabel(w)
    #png=QtGui.QPixelFormat('C:\Users\simet\Desktop\untitled.jpg')
    #photo.setPixmap(png)
    
    #establish the vedio window
    thread = QtCore.QThread()
    thread.start()
    vid = ShowVideo()
    vid.moveToThread(thread)
    image_viewer = GUI()
 
    vid.VideoSignal.connect(image_viewer.setImage)
 
    #This is to set up the layout of the vedio player
    push_button1 =QtWidgets.QPushButton('Start')
    push_button1.clicked.connect(vid.startVideo)
    vertical_layout = QtWidgets.QVBoxLayout()
    
 
    vertical_layout.addWidget(image_viewer)
    vertical_layout.addWidget(push_button1)
 
    layout_widget = QtWidgets.QWidget()
    layout_widget.setLayout(vertical_layout)
 
    main_window = QtWidgets.QMainWindow()
    main_window.setCentralWidget(layout_widget)
    main_window.show()
    sys.exit(app.exec_())
   
