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
        self.E1 = wpilib.VictorSP(0) #Left Elevator Motor
        self.E2 = wpilib.VictorSP(1) #Right Elevatror Motor
        self.S1 = wpilib.VictorSP(2) #Left Shoulder Motor
        self.S2 = wpilib.VictorSP(3) #Right Shoulder Motor
        self.M0 = ctre.wpi_talonsrx.WPI_TalonSRX(4)
        self.M1 = ctre.wpi_talonsrx.WPI_TalonSRX(3)
        self.M0.setInverted(True)
        self.M1.setInverted(True)
        self.left = wpilib.SpeedControllerGroup(self.M0,self.M1)
        self.M2 = ctre.wpi_talonsrx.WPI_TalonSRX(2)
        self.M3 = ctre.wpi_talonsrx.WPI_TalonSRX(1)
        self.right = wpilib.SpeedControllerGroup(self.M2, self.M3)
        self.drive = wpilib.drive.DifferentialDrive(self.left,self.right)
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
        self.drive.arcadeDrive(-1*self.stick.getRawAxis(0), self.stick.getRawAxis(1))
        if self.stick.getRawButton(1) == True and self.stick.getRawButton(2) == False:
            self.E1.set(0.4)
            self.E2.set(-0.4)
        elif self.stick.getRawButton(2) == True and self.stick.getRawButton(1) == False:
            self.E1.set(-0.4)
            self.E2.set(0.4)
        else:
            self.E1.set(0)
            self.E2.set(0)
        if self.stick.getRawButton(3) == True and self.stick.getRawButton(4) == False:
            self.S1.set(0.4)
            self.S2.set(-0.4)
        elif self.stick.getRawButton(4) == True and self.stick.getRawButton(3) == False:
            self.S1.set(-0.4)
            self.S2.set(0.4)
        else:
            self.S1.set(0)
            self.S2.set(0)

if __name__ == "__main__":
    wpilib.run(MyRobot)
