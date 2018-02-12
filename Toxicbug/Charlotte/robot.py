#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 12:11:36 2018

@author: chenquancheng
"""
#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""

import wpilib
import wpilib.drive
import ctre

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.M0 = ctre.wpi_talonsrx.WPI_TalonSRX(4)
        self.M1 = ctre.wpi_talonsrx.WPI_TalonSRX(3)
        self.left = wpilib.drive.DifferentialDrive(self.M0,self.M1)
        self.M2 = ctre.wpi_talonsrx.WPI_TalonSRX(2)
        self.M3 = ctre.wpi_talonsrx.WPI_TalonSRX(1)
        self.right = wpilib.drive.DifferentialDrive(self.M2, self.M3)
        self.stick = wpilib.Joystick(0)
        self.timer = wpilib.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Drive for two seconds
        if self.timer.get() < 2.0:
            self.drive.arcadeDrive(-0.5, 0)  # Drive forwards at half speed
        else:
            self.drive.arcadeDrive(0, 0)  # Stop robot

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drive.arcadeDrive(-1*self.stick.getY(), self.stick.getX())


if __name__ == "__main__":
    wpilib.run(MyRobot)