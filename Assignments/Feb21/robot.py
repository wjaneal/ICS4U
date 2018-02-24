#This is a good foundation to build your robot code on


import wpilib
import wpilib.drive
from networktables import NetworkTables
import dashboard

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        
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
        
        #Dashboard
        NetworkTables.initialize(server='10.61.62.2')

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
        """This function is called periodically during operator control."""
        #self.drive.arcadeDrive(-1*self.stick.getRawAxis(0), self.stick.getRawAxis(1))
        self.drive.arcadeDrive(self.stick.getY(), self.stick.getX())
        #Camera Point Front:
        if self.stick.getPOV()==0:
            self.SV1.set(1.0)
        #Camera Point Back:
        if self.stick.getPOV()==180:
            self.SV1.set(-1.0)
        #Dashboard
        self.sd.putNumber('speed', 0.5)
        self.sd.putValue("Camera", "Forwards")

if __name__ == "__main__":
    wpilib.run(MyRobot)
