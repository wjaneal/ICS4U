#!/usr/bin/en5v python3
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
        #Camera:
        wpilib.CameraServer.launch()
	#Counters
        self.getCubeCounter = 0
        self.dropCubeCounter = 0
        self.elevatorDownCounter = 0
        self.elevatorUpCounter = 0
        self.cubeTravelUp = 50
        self.cubeTravelStop = 1

        #Drive Factor - adjust controller reponsiveness
        self.driveFactor = 0.5

        #Encoders - left and right, attached to gearbox
        self.leftEncoder = wpilib.Encoder(4,5)
        self.rightEncoder = wpilib.Encoder(6,7)

        # Pneumatics:
        self.leftGearShift = wpilib.Solenoid(5,0)
        self.rightGearShift = wpilib.Solenoid(5,1)
        self.goldenArrowhead = wpilib.Solenoid(5,2) # Reference to Guyanese flag

        # Include limit switches for the elevator and shoulder mechanisms
        # 2018-2-16 Warning! The Switch's channel should be modified according to the robot! - Fixed
        self.SW0 = wpilib.DigitalInput(0) #Lower Elevator Switch
        self.SW1 = wpilib.DigitalInput(1) #Upper Elevator Switch
        self.SW2 = wpilib.DigitalInput(2) #Lower shoulder switch
        self.SW3 = wpilib.DigitalInput(3) #Upper shoulder switch

        # Left Motor Group Setup
        self.M0 = ctre.wpi_talonsrx.WPI_TalonSRX(4)
        self.M1 = ctre.wpi_talonsrx.WPI_TalonSRX(3)
        self.M0.setInverted(True)
        self.M1.setInverted(True)
        self.left = wpilib.SpeedControllerGroup(self.M0,self.M1)

        # Right Motor Group Setup
        self.M2 = ctre.wpi_talonsrx.WPI_TalonSRX(2)
        self.M3 = ctre.wpi_talonsrx.WPI_TalonSRX(1)
        self.right = wpilib.SpeedControllerGroup(self.M2,self.M3)

        # Drive setup
        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)
        self.drive.setMaxOutput(self.driveFactor)

        # Misc Setting
        self.stick = wpilib.Joystick(0)
        self.timer = wpilib.Timer()

        # E = Elevator
        self.E1 = wpilib.VictorSP(0)
        self.E2 = wpilib.VictorSP(1)
        # Shoulder
        self.S1 = wpilib.VictorSP(2)
        self.S2 = wpilib.VictorSP(3)
        #Servo
        #channel number!
        self.SV1 = wpilib.Servo(4)
        #self.SV2 = wpilib.Servo(5)
        #self.SV1.set(0.0)
        #self.SV2.set(0.0)



    def autonomousInit(self):
        pass
        """This function is run once each time the robot enters autonomous mode."""
        #self.timer.reset()
        #self.timer.start()
        #self.EC1.reset()
        #self.EC2.reset()
        #self.EC1.setDistancePerPulse(0.01)        
        
            
    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Drive for two seconds

        if self.leftEncoder.getDistance() <= 1.0:
            self.drive.arcadeDrive(-0.5, 0)
        else:
            self.drive.arcadeDrive(0,0)
        #self.EC1.getRate() - Get the current rate of the encoder. Units are distance per second as scaled by the value from setDistancePerPulse().

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
	
	#Set the maximum output of the drive based on the left trigger:
        self.drive.setMaxOutput(1.0-self.stick.getRawAxis(3))
        # Drive setting - use left stick for forward drive and right stick for backward drive
        #if self.stick.getRawAxis(4)==0 and self.stick.getRawAxis(5)==0:
        self.drive.arcadeDrive(-1*self.stick.getRawAxis(0), self.stick.getRawAxis(1))
        #if self.stick.getRawAxis(0)==0 and self.stick.getRawAxis(1)==0:
        #    self.drive.arcadeDrive(-1*self.stick.getRawAxis(4),self.stick.getRawAxis(5))

        # Elevator
        # 2018-2-16 Warning! The Switch number should be modified accroding to the robot! - Fixed
        if self.stick.getRawButton(1) == True: # & self.SW0.get() == False & self.SW1.get() == False:
            self.E1.set(1)
            self.E2.set(-1)
        elif self.stick.getRawButton(2) == True: #& self.SW2.get() == False & self.SW3.get() == False:
            self.E1.set(-1)
            self.E2.set(1)
        else:
            self.E1.set(0)
            self.E2.set(0)

        # Shoulder
        if self.stick.getRawButton(3)==True:
            self.S1.set(0.25)
            self.S2.set(0.25)
        elif self.stick.getRawButton(4)==True:
            self.S1.set(-0.25)
            self.S2.set(-0.25)
        else:
            self.S1.set(0)
            self.S2.set(0)

        #Pneumatics
	#Powercube collector - "Golden Arrowhead"
        if self.stick.getRawButton(5)==True:
            self.goldenArrowhead.set(True)
        elif self.stick.getRawButton(6)==True:
            self.goldenArrowhead.set(False)
        
	#Shift Gears
        if self.stick.getRawButton(7)==True:
            self.leftGearShift.set(True)
            self.rightGearShift.set(True)
        elif self.stick.getRawButton(8)==True:
            self.leftGearShift.set(False)
            self.rightGearShift.set(False)
        #Camera Point Front:
        if self.stick.getPOV()==0:
            self.SV1.set(1.0)
	#Camera Point Back:
        if self.stick.getPOV()==180:
            self.SV1.set(-1.0)
        #State Machine
        if self.stick.getPOV()==270:
           self.getCubeCounter = 51
        if self.stick.getPOV()==90:
            self.elevatorDownCounter = 51
        if self.stick.getPOV() == 135:
            self.elevatorUpCounter = 51

        if self.getCubeCounter>0:
            self.getCube()
            self.getCubeCounter-=1
        if self.dropCubeCounter>0:
            self.dropCube()
            self.dropCubeCounter-=1
        #if self.stick.getRawbutton(5):
        #   self.state_machine.engage()
        #if self.joystick.getRawButton(6):
        #   self.state_machine.done()
       
    #This function attempts to execute a state machine
    def getCube(self):
        #Check that bottom limit switch is on.  If it is not, kill the procedure:
        if self.SW0.get() == True:
            self.getCubeCounter = 0
        #Grab the Cube (False position)
        if self.getCubeCounter==self.cubeTravelUp:
            self.goldenArrowhead.set(False)
        #Move elevator up:
        if self.getCubeCounter<self.cubeTravelUp and self.getCubeCounter>self.cubeTravelStop:
            self.E1.set(-0.8)
            self.E2.set(0.8)
        #If the top limit switch is set, stop the procedure:
        if self.SW1.get() == True:
            self.getCubeCounter = 0
        return 1.0

    # This function attempts to execute a state machine
    def dropCube(self):
        if self.dropCubeCounter < 50 and self.dropCubeCounter > 5:
            self.S1.set(-0.25)
            self.S2.set(-0.25)
        if self.dropCubeCounter == 1:
            self.goldenArrowhead.set(True)
        return 1.0

    def elevatorDown(self):
        if self.SW0.get()==False:
            elevatorDownCounter = 0
        else:
            self.E1.set(-0.2)
            self.E2.set(0.2)

    def elevatorUp(self):
        if self.SW1.get()==True:
            elevatorDownCounter = 0
        else:
            self.E1.set(0.2)
            self.E2.set(-0.2)
if __name__ == "__main__":
    wpilib.run(MyRobot)

