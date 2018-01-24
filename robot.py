#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:31:49 2017

@author: chenquancheng
"""

#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""

import wpilib
#from networktables import NetworkTables
#wpilib - contains many classes and functions 
#for programming FRC robots.
#wpilib.IterativeRobot - this is a base robot class.
#MyRobot builds on the base class
#We add functions to the base class below.
class MyRobot(wpilib.IterativeRobot): #Builds on a base class

    def robotInit(self): #This is a function or method
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.robot_drive = wpilib.RobotDrive(0,1, 2, 3)
        self.setInvertedMotor(0, True)
        self.setInvertedMotor(1, True)
        self.setInvertedMotor(2, True)
        self.setInvertedMotor(3, True)
        self.stick = wpilib.Joystick(0)
        self.Motor1 = wpilib.VictorSP(0)
        self.Motor2 = wpilib.VictorSP(1)
        #self.Switch1 = wpilib.DigitalInput(0)
        #self.Switch2 = wpilib.DigitalInput(1)
        #self.Servo1 = wpilib.Servo(6)
        #self.Servo2 = wpilib.Servo(7)
        # As a client to connect to a robot
        #NetworkTables.initialize(server='10.61.62.103')
        #sd = NetworkTables.getTable('SmartDashboard')
        #sd.putNumber('someNumber', 1234)
        #otherNumber = sd.getNumber('otherNumber')
    
    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.auto_loop_counter = 0

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        # Check if we've completed 100 loops (approximately 2 seconds)
        if self.auto_loop_counter < 100:
            self.robot_drive.drive(-0.5, 0) # Drive forwards at half speed
            self.auto_loop_counter += 1
        else:
            self.robot_drive.drive(0, 0)    #Stop robot

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.robot_drive.arcadeDrive(self.stick)
        '''if self.stick.getRawButton(1)==True:
            self.Motor1.set(1.0)
            self.Motor2.set(-1.0)
        if self.stick.getRawButton(2)==True:
            self.Motor1.set(-1.0)
            self.Motor2.set(1.0)
        if self.stick.getRawButton(3)==True:
            self.Motor1.set(-0.8)
            self.Motor2.set(0.8)
        if self.stick.getRawButton(4)==True:
            self.Motor1.set(0.8)
            self.Motor2.set(-0.8)
        if self.stick.getRawButton(1)==False and self.stick.getRawButton(2) == False and self.stick.getRawButton(3)==False and self.stick.getRawButton(4) == False:
            self.Motor1.set(0)
            self.Motor2.set(0)'''
	    #This number ranges from -1 to 1-fully reverse to fully forward
            #self.Servo1.set(0.8) #This number ranges from 0 to 1-fully left to fullt right
        '''else:
            self.Motor1.set(stick.getRawAxis(2)) 
            self.Servo1.set(0.4)
        if self.Switch2.get()==True:
            self.Motor2.set(1)
            self.Servo2.set(0.8)
        else:
            self.Motor2.set(0)
            self.Servo2.set(0.4)
'''
    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()

if __name__ == "__main__":
    wpilib.run(MyRobot)
