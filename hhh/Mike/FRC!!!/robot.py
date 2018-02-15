#!/usr/bin/env python3

import wpilib
import ctre


class MyRobot(wpilib.IterativeRobot):
    '''
        This is a short sample program demonstrating how to use the basic throttle
        mode of the TalonSRX
    '''

    def robotInit(self):
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
        if self.stick1.getRawButton(1)==True:
            self.motor1.set(0.5)
            self.motor2.set(0.5)
            self.motor3.set(0.5)
            self.motor4.set(0.5)
        else:
            self.motor1.set(0)
            self.motor2.set(0)
            self.motor3.set(0)
            self.motor4.set(0)
     


if __name__ == '__main__':
    wpilib.run(MyRobot)
