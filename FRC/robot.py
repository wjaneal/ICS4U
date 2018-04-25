#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""
import ctre
import wpilib
import wpilib.drive


class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.gearShiftLeft = wpilib.Solenoid(5,0)
        self.gearShiftRight = wpilib.Solenoid(5,1)
        self.switch1 = wpilib.DigitalInput(0)
        self.switch2 = wpilib.DigitalInput(1)
        self.M0 = ctre.wpi_talonsrx.WPI_TalonSRX(4)
        self.M1 = ctre.wpi_talonsrx.WPI_TalonSRX(3)
        self.M0.setInverted(True)
        self.M1.setInverted(True)
        self.left = wpilib.SpeedControllerGroup(self.M0,self.M1)
        self.M2 = ctre.wpi_talonsrx.WPI_TalonSRX(2)
        self.M3 = ctre.wpi_talonsrx.WPI_TalonSRX(1)
        self.right = wpilib.SpeedControllerGroup(self.M2,self.M3)
        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)
        self.stick = wpilib.Joystick(0)
        self.timer = wpilib.Timer()
        self.E1 = wpilib.VictorSP(0)
        self.E2 = wpilib.VictorSP(1)
        self.S1 = wpilib.VictorSP(2)
        self.S2 = wpilib.VictorSP(3)
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
        if self.stick.getRawButton(1) == True and self.switch2.get()==False:
            self.E1.set(0.8)
            self.E2.set(-0.8)
        elif self.stick.getRawButton(2) == True and self.switch1.get()==True:
            self.E1.set(-0.8)
            self.E2.set(0.8)
        else:
            self.E1.set(0)
            self.E2.set(0)
        if self.stick.getRawButton(3)==True:
            self.S1.set(-0.4)
            self.S2.set(-0.4)
            self.gearShiftLeft.set(False) 
            self.gearShiftRight.set(False)
        elif self.stick.getRawButton(4)==True:
            self.S1.set(0.4)
            self.S2.set(0.4)
            self.gearShiftLeft.set(True)
            self.gearShiftRight.set(True)
        else:
            self.S1.set(0)
            self.S2.set(0)
if __name__ == "__main__":
    wpilib.run(MyRobot)

