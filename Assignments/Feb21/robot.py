#This is a good foundation to build your robot code on


import wpilib
import wpilib.drive
from networktables import NetworkTables
#import dashboard

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """

        self.prepareCubeFlag = 0

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
 
        self.stick = wpilib.Joystick(0)
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
    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
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
       
    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        
        for i in self.dataSet:
            if i[4][0] < self.timer.get() and self.timer.get() <= i[4][1]:
                self.drive.arcadeDrive(i[0],i[1])
                self.SV1.set(i[3])
                self.sd.putValue("Camera",i[5])
            else:
                self.drive.arcadeDrive(0,0)
        
    def teleopPeriodic(self):
        self.drive.setMaxOutput(0.5)
        self.sd.putValue("SW2", self.SW2.get())
        self.sd.putValue("SW1", self.SW1.get())
        """This function is called periodically during operator control."""
        #self.drive.arcadeDrive(-1*self.stick.getRawAxis(0), self.stick.getRawAxis(1))
        self.drive.arcadeDrive(self.stick.getY(), self.stick.getX())
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
        #Dashboard
        self.sd.putNumber('speed', 0.5)
        '''
        self.sd.putNumber('speed', 0.5)
        self.sd.putValue("Camera", "Forwards")
        '''
        if self.stick.getRawButton(1) == True:
            self.prepareCubeFlag = 1
            if self.prepareCubeFlag > 0:
                self.prepareGrabCube()
        if self.stick.getRawButton(2) == True:
            self.grabCubeFlag = 1
            if self.grabCubeFlag > 0:
                self.grabCube()
            self.grabCube()
        if self.stick.getRawButton(3) == True:
            self.deliverCubeFlag = 1
            if self.deliverCubeFlag > 0:   
                self.deliverCube()
        if self.stick.getRawButton(5) == True:
            self.adjustLeftFlag = 1
            if self.adjustLeftFlag > 0:
                self.AdjustElevatorLeft()
        if self.stick.getRawButton(6) == True:
            self.adjustRightFlag = 1
            if self.adjustRightFlag > 0:
                self.AdjustElevatorRight()
    
    def prepareGrabCube(self):
    #(1)Check that the lower elevator switch is on - elevator at bottom
	#(2)If not, move elevator to bottom (and arms to bottom)
        if self.SW0.get()==True:
            self.SV2.set(0.25)
            self.E.set(0.5)
        self.prepareCubeFlag +=1
        if self.SW0.get()==False or self.prepareCubeFlag > 50:
            self.SV2.set(-0.25)
            self.E.set(0)
            self.prepareCubeFlag = 0

    def grabCube(self):
    #(1)Grab cube
    #(2) Move cube up until it hits the top (or part way up????)
        self.SV2.set(-0.5)
        if self.SW1.get() == True:
            self.E.set(-0.5)
        if self.SW1.get() == False:
            self.E.set(0)
            self.grabCubeFlag = 0
       
    def deliverCube(self):
        if self.SW0.get() == True:
            self.E.set(0.5)
        if self.SW0.get() == False:
            self.SV2.set(0.5)
            self.E.set(0)
            self.deliverCubeFlag = 0
            
    def AdjustElevatorLeft(self):
        if self.SW1.get() == True:
            self.E.set(0.25)
        if self.SW1.get() == False:
            self.E.set(0)
            self.adjustLeftFlag=0
        
    def AdjustElevatorRight(self):
        if self.SW1.get() == True:
            self.E.set(-0.25)
        if self.SW1.get() == False:
            self.E.set(0)
            self.adjustRightFlag=0
        
            
        
        

if __name__ == "__main__":
    wpilib.run(MyRobot)
