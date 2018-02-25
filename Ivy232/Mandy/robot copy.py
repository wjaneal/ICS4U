#This is a good foundation to build your robot code on


import wpilib
import wpilib.drive


class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """

        #Set up motors to drive robot
        self.M2 = wpilib.VictorSP(2)
        self.M3 = wpilib.VictorSP(3)
        #self.M2.setInverted(True)
        #self.M3.setInverted(True)
        self.left = wpilib.SpeedControllerGroup(self.M2,self.M3)
        
        self.M0 = wpilib.VictorSP(0)
        self.M1 = wpilib.VictorSP(1)
        self.SV1 = wpilib.Servo(8)
        self.SV2 = wpilib.Servo(9)
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
        if self.SW1.get() == True:
            self.getCubeCounter = 0
            
        #Camera Point Front:
        if self.stick.getPOV()==0:
            self.SV1.set(1.0)
	#Camera Point Back:
        if self.stick.getPOV()==180:
            self.SV1.set(-1.0)
            
        if self.timer.get() < 3.3:
            self.drive.arcadeDrive(-0.5, 0)  # Drive forwards at half speed: (-0.5)
        elif self.timer.get() <= 6.3:
            self.drive.arcadeDrive(-0.5, -0.5)  # Turn left
                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        if self.timer.get() >= 6.3 and self.timer.get() <= 14 :
            self.drive.arcadeDrive(-0.5, 0)
            self.drive.arcadeDrive(-0.5, 1)  # turn around: (1)
            self.drive.arcadeDrive(0, 0)  # Stop robot
            self.Servo.set(0.5)
        

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drive.arcadeDrive(self.stick.getY(), self.stick.getX())


if __name__ == "__main__":
    wpilib.run(MyRobot)
