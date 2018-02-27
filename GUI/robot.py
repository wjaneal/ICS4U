#This is a good foundation to build your robot code on


import wpilib
import wpilib.drive
from networktables import NetworkTables
import logging
class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        #Initialize the network table
        NetworkTables.initialize()
        logging.basicConfig(level=logging.DEBUG)#What is this?
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
        
    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Drive for two seconds
        if self.timer.get() < 3.0:
            self.drive.arcadeDrive(0.1,0.1)  # Drive forwards at half speed
            Left = 0.1
            Right = 0.1
            '''
        if self.timer.get() >=3 and self.timer.get() <=6:
            self.drive.arcadeDrive(-0.5,-0.5)
            Left = -0.5
            Right = -0.5       
        if self.timer.get()>6 and self.timer.get() < 7:
            self.drive.arcadeDrive(-0.5, 0)
            Left = -0.5
            Right = 0        
        if self.timer.get()>7:
            self.drive.arcadeDrive(0,0)
            Left = 0
            Right = 0
        
        if self.timer.get() >= 3 and self.timer.get() <= 6:
            self.drive.arcadeDrive(-0.5,-0.5)
            Left = -0.5
            Right = -0.5       
        if self.timer.get() > 6 and self.timer.get() < 7:
            self.drive.arcadedrive(-0.5,0)
            Left = -0.5
            Right = 0        
        if self.timer.get() > 7:
            self.drive.arcadeDrive(0, 0)  # Stop robot
        # Networktable
        '''
        sd = NetworkTables.getTable("SmartDashboard")
        sd.putNumber('Left',Left)
        sd.putNumber('Right',Right)
    def teleopPeriodic(self):

        
        
        """This function is called periodically during operator control."""
        #self.drive.arcadeDrive(-1*self.stick.getRawAxis(0), self.stick.getRawAxis(1))

if __name__ == "__main__":
    wpilib.run(MyRobot)
