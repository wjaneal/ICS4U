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
from CSCore import CameraServer
class ShowVideo(QtCore.QObject):
 
    #initiating the built in camera
    #camera_port = 0
    #camera = cv2.VideoCapture(camera_port)
    VideoSignal = QtCore.pyqtSignal(QtGui.QImage)
    
 
    def __init__(self, parent = None):
        super(ShowVideo, self).__init__(parent)
        self.ip='10.61.62.3'
    @QtCore.pyqtSlot()
    def startVideo(self):
        cs = CameraServer.getInstance()
        run_video = True
        while run_video:
            self.cap = cs.getVideo("Camera", 320, 240)
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
        
        self.lat=QtWidgets.QLabel(self)
        self.lat.setGeometry(30,180,120,25)
        self.lat.setText('autonomous type')
        
        self.atbt1 = QPushButton(self)
        self.atbt1.setGeometry(130,180,50,25)
        self.atbt1.setText('1')
        self.atbt1.clicked.connect(self.changeat1)
        
        self.atbt1 = QPushButton(self)
        self.atbt1.setGeometry(190,180,50,25)
        self.atbt1.setText('2')
        self.atbt1.clicked.connect(self.changeat2)
        
        self.atbt1 = QPushButton(self)
        self.atbt1.setGeometry(250,180,50,25)
        self.atbt1.setText('3')
        self.atbt1.clicked.connect(self.changeat3)
        
        self.atbt1 = QPushButton(self)
        self.atbt1.setGeometry(310,180,50,25)
        self.atbt1.setText('4')
        self.atbt1.clicked.connect(self.changeat4)
        self.setGeometry(0, 100, 1500, 1000)
        self.setWindowTitle('Input dialog')
        self.show()
        
        self.M0= QProgressBar(self)
        self.M0.setGeometry()
        self.M1= QProgressBar(self)
        self.M2= QProgressBar(self)
        self.M3= QProgressBar(self)

        
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



        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    thread = QtCore.QThread()
    thread.start()
    vid = ShowVideo()
    vid.moveToThread(thread)
    image_viewer = GUI()
 
    vid.VideoSignal.connect(image_viewer.setImage)
 
    #Button to start the videocapture:
 
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
    #app = QApplication(sys.argv)
    ex = GUI()
    sys.exit(app.exec_())