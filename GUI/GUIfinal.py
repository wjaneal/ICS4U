import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar, 
    QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
from networktables import NetworkTables 
import logging
logging.basicConfig(level=logging.DEBUG)
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
import cv2
class ShowVideo(QtCore.QObject):
 
    
    VideoSignal = QtCore.pyqtSignal(QtGui.QImage)
    
 
    def __init__(self, parent = None):
        super(ShowVideo, self).__init__(parent)
        self.ip='10.61.62.20:8081'
    @QtCore.pyqtSlot()
    def startVideo(self):
        #cs = CameraServer.getInstance()
        run_video = True
        while run_video:
            self.cap = cv2.VideoCapture("http://"+ str(self.ip)+":8081/?action=stream?dummy=param.mjpg")

            ret, image = self.cap.read()
 
            color_swapped_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
            height, width, _ = color_swapped_image.shape
            
            #width = camera.set(CAP_PROP_FRAME_WIDTH, 1600)
			#height = camera.set(CAP_PROP_FRAME_HEIGHT, 1080)
			#camera.set(CAP_PROP_FPS, 15)
 
            qt_image = QtGui.QImage(color_swapped_image.data,
                                    width,
                                    height,
                                    color_swapped_image.strides[0],
                                    QtGui.QImage.Format_RGB888)
 
            self.VideoSignal.emit(qt_image)
class GUI(QWidget):

    def __init__(self,parent = None):
        super().__init__()
        self.ip='10.61.62.3'

        #self.timer_camera = QtCore.QTimer()
        self.initUI()
        self.cap = cv2.VideoCapture("http://"+ str(self.ip) +":8081/?action=stream?dummy=param.mjpg")
        self.CAM_NUM = 0
        super(GUI, self).__init__(parent)
        self.image = QtGui.QImage()
        self.setAttribute(QtCore.Qt.WA_OpaquePaintEvent)
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(0,0, self.image)
        self.image = QtGui.QImage()
    def setImage(self, image):
        if image.isNull():
            print("Viewer Dropped frame!")
 
        self.image = image
        if image.size() != self.size():
            self.setFixedSize(image.size())
        self.update()
        
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
        self.Elv1=QtWidgets.QLabel(self)
        self.Elv1.setGeometry(500,150,200,50)
        self.Elv1.setText('Elevators')
        
        
        self.elv2 = QPushButton(self)
        self.elv2.setGeometry(600,100,50,50)
        
        self.Left = QPushButton(self)
        self.Left.setGeometry(150,20,50,50)
        self.Left.setText('L')
        
        self.Right = QPushButton(self)
        self.Right.setGeometry(250,20,50,50)
        self.Right.setText('R')
        
        self.dist = QPushButton(self)
        self.dist.setGeometry(20,670,100,50)
        self.dist.setText('Distance:')
        
        self.time = QPushButton(self)
        self.time.setGeometry(340,670,100,50)
        self.time.setText('Time:')
        
        self.dist1 = QPushButton(self)
        self.dist1.setGeometry(140,670,100,50)
        self.dist2 = QPushButton(self)
        self.dist2.setGeometry(140,750,100,50)
        
        self.time1 = QPushButton(self)
        self.time1.setGeometry(460,670,100,50)
        self.time2 = QPushButton(self)
        self.time2.setGeometry(460,750,100,50)
        
        
        
        self.auto1 = QPushButton(self)
        self.auto1.setGeometry(600,670,40,40)
        self.auto1.setText('colour')
        self.auto1.clicked.connect(self.A1)        
        self.auto2 = QPushButton(self)
        self.auto2.setGeometry(640,670,40,40)
        self.auto2.clicked.connect(self.A2)
        self.auto2.setText('1')
        self.auto3 = QPushButton(self)
        self.auto3.setGeometry(680,670,40,40)
        self.auto3.setText('2')
        self.auto3.clicked.connect(self.A3)
        self.auto4 = QPushButton(self)
        self.auto4.setGeometry(720,670,40,40)
        self.auto4.setText('start')
        self.auto4.clicked.connect(self.A4)
        self.auto5 = QPushButton(self)
        self.auto5.setGeometry(760,670,40,40)
        self.auto5.setText('1')
        self.auto5.clicked.connect(self.A5)
        self.auto6 = QPushButton(self)
        self.auto6.setGeometry(800,670,40,40)
        self.auto6.setText('2')
        self.auto6.clicked.connect(self.A6)
        self.auto7 = QPushButton(self)
        self.auto7.setGeometry(840,670,40,40)
        self.auto7.setText('3')
        self.auto7.clicked.connect(self.A7)
        '''
        self.auto8 = QPushButton(self)
        self.auto8.setGeometry(880,670,40,40)
        self.auto8.setText('8')
        self.auto8.clicked.connect(self.A8)
        self.auto9 = QPushButton(self)
        self.auto9.setGeometry(920,670,40,40)
        self.auto9.setText('9')
        self.auto9.clicked.connect(self.A9)
        self.auto10 = QPushButton(self)
        self.auto10.setGeometry(960,670,40,40)
        self.auto10.setText('10')
        self.auto10.clicked.connect(self.A10)
        self.auto11 = QPushButton(self)
        self.auto11.setGeometry(1000,670,40,40)
        self.auto11.setText('11')
        self.auto11.clicked.connect(self.A11)
        self.auto12 = QPushButton(self)
        self.auto12.setGeometry(1040,670,40,40)
        self.auto12.setText('12')
        self.auto12.clicked.connect(self.A12)
        '''
        self.ToBe = QPushButton(self)
        self.ToBe.setGeometry(800,750,100,50)
        self.ToBe.setText('not running')
        self.driNum = QPushButton(self)
        self.driNum.setGeometry(800,250,50,50)
        self.Gyro=QPushButton(self)
        self.Gyro.setGeometry(900,320,50,50)
        self.Gyro.setText('0')
        self.ArmState=QPushButton(self)
        self.ArmState.setGeometry(1000,390,200,50)
        self.ArmState.setText('not sure')
        
        self.gyro = QtWidgets.QLabel(self)
        self.gyro.setGeometry(900,250,100,50)
        self.gyro.setText('gyro:')
        self.arm = QtWidgets.QLabel(self)
        self.arm.setGeometry(1000,320,100,50)
        self.arm.setText('arm:')
        self.AutoMATA = QtWidgets.QLabel(self)
        self.AutoMATA.setGeometry(600,750,250,50)
        self.AutoMATA.setText('Current autonomous code:')
        self.driFac= QtWidgets.QLabel(self)
        self.driFac.setGeometry(800,170,200,50)
        self.driFac.setText('driver factor:')
        
        
        
        
        
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

        '''        
        self.timer = QBasicTimer()
        self.step = 0
        self.timer.start(100, self)
        
        self.setGeometry(100, 100, 1500, 900)
        self.setWindowTitle('Input dialog')
        
        
        self.show()
        
        
    def timerEvent(self, e):
        
        NetworkTables.initialize(server='10.61.62.2')
        self.sd = NetworkTables.getTable("SmartDashboard")
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
    
    def A1(self):
        print('clicked')
        self.sd.putNumber('colour',0)
        self.ToBe.setText('1')
    def A2(self):
        print('clicked')
        self.sd.putNumber('colour',1)
        self.ToBe.setText('2')
    def A3(self):
        print('clicked')
        self.sd.putNumber('colour',2)
        self.ToBe.setText('3')
    def A4(self):
        print('clicked')
        self.sd.putNumber('start',0)
        self.ToBe.setText('4')
    def A5(self):
        print('clicked')
        self.sd.putNumber('start',1)
        self.ToBe.setText('5')
    def A6(self):
        print('clicked')
        self.sd.putNumber('start',2)
        self.ToBe.setText('6')
    def A7(self):
        print('clicked')
        self.sd.putNumber('start',3)
        self.ToBe.setText('7')
    '''
    def A8(self):
        print('clicked')
        self.sd.putNumber('auto',8)
        self.ToBe.setText('8')
    def A9(self):
        print('clicked')
        self.sd.putNumber('auto',9)
        self.ToBe.setText('9')
    def A10(self):
        print('clicked')
        self.sd.putNumber('auto',10)
        self.ToBe.setText('10')
    def A11(self):
        print('clicked')
        self.sd.putNumber('auto',11)
        self.ToBe.setText('11')
    def A12(self):
        print('clicked')
        self.sd.putNumber('auto',12)
        self.ToBe.setText('12')
    '''
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    thread = QtCore.QThread()
    thread.start()
    vid = ShowVideo()
    vid.moveToThread(thread)
    image_viewer = GUI()
 
    vid.VideoSignal.connect(image_viewer.setImage)
 
 
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
    ex = GUI()
    sys.exit(app.exec_())