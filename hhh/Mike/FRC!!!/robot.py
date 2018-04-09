#!/usr/bin/env python3

import wpilib
import ctre


class MyRobot(wpilib.IterativeRobot):
    '''
        This is a short sample program demonstrating how to use the basic throttle
        mode of the TalonSRX
    '''

    def robotInit(self):
        self.robot_drive = wpilib.RobotDrive(5,6)
        self.stick1 = wpilib.Joystick(0)

        self.motor1 = ctre.WPI_TalonSRX(1) # Initialize the TalonSRX on device 1.
        self.motor2 = ctre.WPI_TalonSRX(2)
        self.motor3 = ctre.WPI_TalonSRX(3)
        self.motor4 = ctre.WPI_TalonSRX(4)
        

    def disabledPeriodic(self):
        self.motor1.disable()

    def teleopPeriodic(self):
        # Set the motor's output to half power.
        # This takes a number from -1 (100% speed in reverse) to +1 (100%
        # speed going forward)
        if self.stick.getRawButton(1)==True:
            self.Motor1.set(1.0)
            self.Motor2.set(-1.0)
        if self.stick.getRawButton(2)==True:
            self.Motor1.set(-1.0)
            self.Motor2.set(1.0)
        if self.stick.getRawButton(3)==True:
            self.Motor1.set(-1.0)
            self.Motor2.set(1.0)
        if self.stick.getRawButton(4)==True:
            self.Motor1.set(1.0)
            self.Motor2.set(-1.0)
        if self.stick.getRawButton(1)==False and self.stick.getRawButton(2) == False and self.stick.getRawButton(3)==False and self.stick.getRawButton(4) == False:
            self.Motor1.set(0)
            self.Motor2.set(0)
    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()    
     


if __name__ == '__main__':
    wpilib.run(MyRobot)
