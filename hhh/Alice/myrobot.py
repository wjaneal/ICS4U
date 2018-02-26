#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 13:19:38 2018

@author: haichunkan
"""

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
        if self.timer.get() < 0.5:
            self.drive.arcadeDrive(-0.35,0)  # Drive forwards at half speed
        if self.timer.get() >= 0.5 and self.timer.get() <= 1:
            self.drive.arcadeDrive(-0.35,-0.35)
        if self.timer.get() > 1 and self.timer.get() < 1.5:
            self.drive.arcadeDrive(-0.35,0)
        if self.timer.get() >= 1.5 and self.timer.get() <= 2.5:
            self.drive.arcadeDrive(0.35,0.35)
        if self.timer.get() > 2.5 and self.timer.get() < 3:
            self.drive.arcadeDrive(-0.35,0)
        if self.timer.get() > 3:
            self.drive.arcadeDrive(0, 0)  # Stop robot

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        #self.drive.arcadeDrive(-1*self.stick.getRawAxis(0), self.stick.getRawAxis(1))
        self.drive.arcadeDrive(self.stick.getY(), self.stick.getX())

if __name__ == "__main__":
    wpilib.run(MyRobot)