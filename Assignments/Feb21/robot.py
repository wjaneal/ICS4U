#This is a good foundation to build your robot code on


import wpilib
import wpilib.drive
from networktables import NetworkTables

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """

        #Initialize Networktables
        self.sd = NetworkTables.getTable('SmartDashboard')

        
        #Set up motors to drive robot
        self.M2 = wpilib.VictorSP(2)
        self.M3 = wpilib.VictorSP(3)
        #self.M2.setInverted(True)
        #self.M3.setInverted(True)
        self.left = wpilib.SpeedControllerGroup(self.M2,self.M3)
        
        self.M0 = wpilib.VictorSP(0)
        self.M1 = wpilib.VictorSP(1)
        self.right = wpilib.SpeedControllerGroup(self.M0,self.M1)
        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)
        
        
        self.stick = wpilib.Joystick(1)
        self.timer = wpilib.Timer()
        #Camera
        wpilib.CameraServer.launch()
        #Servo
        self.SV1 = wpilib.Servo(9)
        self.SV2 = wpilib.Servo(8)        
        #Dashboard
        NetworkTables.initialize(server='10.61.62.2')
        #Switches
        self.SW0 = wpilib.DigitalInput(0)
        self.SW1 = wpilib.DigitalInput(1)
        #Elevator
        self.E = wpilib.VictorSP(5)
        self.prepareCubeFlag = 0
        self.grabCubeFlag = 0
        self.deliverCubeFlag = 0
        self.adjustLeftFlag=0
        self.adjustRightFlag=0
        self.driveFlag=0
        #Gyro
        self.gyro = wpilib.ADXRS450_Gyro(0)
        self.gyro.reset()
        #All possible autonomous routines in a sendable chooser
        '''
        self.chooser = wpilib.SendableChooser()
        self.chooser.addDefault("None", '4')
        self.chooser.addObject("left-LeftScale", '1')
        self.chooser.addObject("Middle-LeftScale", '2')
        self.chooser.addObject("Right-LeftScale", '3')
        self.chooser.addObject("Left-RightScale", '5')
        '''
        #wpilib.SmartDashboard.putData('Choice', self.chooser)
        #Encoders
        self.EC1 = wpilib.Encoder(2,3)
        self.EC2 = wpilib.Encoder(4,5)
        self.EC1.reset()
        self.EC2.reset()
        
    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        '''
        self.cumulativeTime=0
        self.totalTime=0
        self.dataSet=[[-0.5,0,1,-1.0],[0.3,0.4,1,1.0],[-0.5,0,1,-1.0]]
        for i in self.dataSet:
            self.totalTime+=i[2]
        self.intervals = 0
        self.currentTime = 0
        for i in range(0,len(self.dataSet)):
            self.dataSet[i].append([self.currentTime,self.currentTime+self.dataSet[i][2]])
            self.currentTime+=self.dataSet[i][2]
        for i in self.dataSet:
            if i[3]==1.0:
                i.append("Forward")
            if i[3]==-1.0:
                i.append("Backward")
                
        self.timer.reset()
        self.timer.start()
        '''
        self.timer.reset()
        self.timer.start()
<<<<<<< HEAD
<<<<<<< HEAD
        #self.auto = self.chooser.getSelected()
        self.auto = self.sd.getNumber("auto",0)
        #self.auto = 1
=======
        self.encoder.setDistancePerPulse(0.5)
=======
        self.EC1.reset()
>>>>>>> Charlotteee
        #self.auto = self.chooser.getSelected()
>>>>>>> 9306c022510e8042a2c29ab5812c25dad9f8e24d
    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        '''
        for i in self.dataSet:
            if i[4][0] < self.timer.get() and self.timer.get() <= i[4][1]:
                self.drive.arcadeDrive(i[0],i[1])
                self.SV1.set(i[3])
                self.sd.putValue("Camera",i[5])
            else:
                self.drive.arcadeDrive(0,0)
        '''
<<<<<<< HEAD
<<<<<<< HEAD
        #self.auto = self.sd.getNumber("auto",0)
        #test
        #if(self.auto != 1):
        if(self.auto == 1):
            if self.timer.get() <= 5:           
                self.drive.arcadeDrive(-0.6,0)
                
=======
<<<<<<< HEAD
        auto = sd.getNumber("auto",0)
        #test
        if(self.auto == '1'):
            self.drive.arcadeDrive(0.1,0.1)
=======
        if self.encoder.getDistance() <= 3:
=======
        if self.EC1.getDistance() <= 300:
>>>>>>> Charlotteee
            self.drive.arcadeDrive(-0.6,0)
        else:
            self.drive.arcadeDrive(0,0)
            
            
>>>>>>> Charlotteee
>>>>>>> 9306c022510e8042a2c29ab5812c25dad9f8e24d
    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        #self.drive.arcadeDrive(-1*self.stick.getRawAxis(0), self.stick.getRawAxis(1))
        '''
        if self.stick.getRawButton(7) == True:
            self.driveFlag=0
            self.drive.setMaxOutput(0.5)
        if self.stick.getRawButton(8) == True:
            self.driveFlag=1
            self.driveb = wpilib.drive.DifferentialDrive(self.right, self.left)
            self.driveb.setMaxOutput(0.5)
        if self.driveFlag==1:
            self.driveb.arcadeDrive(self.stick.getRawAxis(5), self.stick.getRawAxis(4))
        '''
        if self.driveFlag==0:
            self.drive.arcadeDrive(self.stick.getRawAxis(1), self.stick.getRawAxis(0))
        
        #Camera Point Front:
        if self.stick.getPOV()==0:
            self.SV1.set(1.0)
            self.sd.putValue('Camera','Forward')
        #Camera Point Back:
        if self.stick.getPOV()==180:
            self.SV1.set(-1.0)
            self.sd.putValue('Camera','Backward')
        #Orient Servo 2
        if self.stick.getPOV()==90:
            self.SV2.set(0.5)
        #Orient Servo 2
        if self.stick.getPOV()==270:
            self.SV2.set(-0.6)
        
        if self.stick.getRawButton(1) == True:
            self.prepareCubeFlag = 1
            self.EC1.reset()
        if self.prepareCubeFlag > 0:
            self.prepareGrabCube()
        if self.stick.getRawButton(2) == True:
            self.grabCubeFlag = 1
            self.EC1.reset()
        if self.grabCubeFlag > 0:
            self.grabCube()
            self.EC2.reset()
        if self.stick.getRawButton(3) == True:
            self.deliverCubeFlag = 1
        if self.deliverCubeFlag > 0:   
            self.deliverCube()
        if self.stick.getRawButton(5) == True:
            self.E.set(-0.3)
        if self.stick.getRawButton(6) == True:
            self.E.set(0.3)
            
        #Dashboard
        self.sd.putNumber('Speed', 0.5)
        self.sd.putNumber('Gyro',self.gyro.getAngle())
        self.sd.putValue("Camera", "Forwards")
        self.sd.putValue("SW1", self.SW1.get())
        self.sd.putValue("SW0", self.SW0.get())
        self.sd.putValue("EC1",self.EC1.getDistance())
        self.sd.putValue("EC2",self.EC2.getDistance())
        
    def prepareGrabCube(self):
    #(1)Check that the lower elevator switch is on - elevator at bottom
	#(2)If not, move elevator to bottom (and arms to bottom)
        if self.EC1.getDistance() <= 1000:
            self.E.set(0.5)
        else:
            self.E.set(0)
            self.prepareCubeFlag = 0

    def grabCube(self):
    #(1)Grab cube
    #(2) Move cube up until it hits the top (or part way up????)
        self.SV1.set(-0.5)
        if self.EC1.getDistance() >= -1000 and self.EC1.getDistance() <= 0:
            self.E.set(-0.5)                     
        else:
            self.E.set(0)
            self.grabCubeFlag = 0
            self.SV1.set(0.5)
            
       
    def deliverCube(self):
        if self.EC2.getDistance() <= 500:
            self.E.set(0.25)
        else:
            self.E.set(0)
            self.SV1.set(0.5)
            self.deliverCubeFlag = 0
            
    
        
            
        
        

if __name__ == "__main__":
    wpilib.run(MyRobot)
