
#!/usr/bin/en5v python3
"""
    This is a good foundation to build your robot code on
"""
import ctre
import wpilib
import wpilib.drive
from wpilib import DriverStation
from networktables import NetworkTables
#from robotpy_ext.autonomous import AutonomousModeSelector



class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        #This initializes Networktables which will be used for communication between our robot and the GUI.
        self.sd = NetworkTables.getTable('SmartDashboard')
        #This initializes the camera.
        wpilib.CameraServer.launch()
        #This sets some counters for the state machines. (FOR Previous version without the encoders)
        #self.getCubeCounter = 0
        #self.dropCubeCounter = 0
        #self.elevatorDownCounter = 0
        #self.elevatorUpCounter = 0
        #self.cubeTravelUp = 50
        #self.cubeTravelStop = 1
        #This sets some flags for the state machines.
        self.prepareCubeFlag=0 #This is the flag for the state machine which makes the robot prepared to grab the cube.
        self.grabCubeFlag=0 #This is the flag for the state machine which makes the robot grab the cube.
        self.deliverCubeFlag=0 #This is the flag for the state machine which makes the robot deliver the cube.
        self.dstate = 0
        self.pstate = 0
        self.gstate = 0
        #This sets the Drive Factor, which adjusts controller responsiveness.
        self.driveFactor = 1
		
        self.auto= self.sd.getNumber("auto",0)
        self.autoState = 0

        #This initializes the Encoders - left and right, attached to gearbox
        self.EC1 = wpilib.Encoder(0,1)
        self.EC2 = wpilib.Encoder(2,3)
        
        #Encoder for the elevator and shoulder
        self.EC3 = wpilib.Encoder(4,5) #This sets the encoder for the elevator.
        self.EC4 = wpilib.Encoder(6,7) #This sets the encoder for the arm.

        #This sets the Pneumatics.
        self.leftGearShift = wpilib.Solenoid(5,0)
        self.rightGearShift = wpilib.Solenoid(5,1)
        self.goldenArrowhead = wpilib.Solenoid(5,2) # Reference to Guyanese flag
        #This controls the function of the arm.
        # Include limit switches for the elevator and shoulder mechanisms
        # 2018-2-16 Warning! The Switch's channel should be modified according to the robot! - Fixed
        #self.SW0 = wpilib.DigitalInput(0) #Lower Elevator Switch
        #self.SW1 = wpilib.DigitalInput(1) #Upper Elevator Switch
        #self.SW2 = wpilib.DigitalInput(2) #Lower shoulder switch
        #self.SW3 = wpilib.DigitalInput(3) #Upper shoulder switch

        # Left Motor Group Setup
        self.M0 = ctre.wpi_talonsrx.WPI_TalonSRX(4)
        self.M1 = ctre.wpi_talonsrx.WPI_TalonSRX(3)
        self.M0.setInverted(True) #This inverts the motors.
        self.M1.setInverted(True)
        self.left = wpilib.SpeedControllerGroup(self.M0,self.M1)

        # Right Motor Group Setup
        self.M2 = ctre.wpi_talonsrx.WPI_TalonSRX(2)
        self.M3 = ctre.wpi_talonsrx.WPI_TalonSRX(1)
        #self.M2.setInverted(True)
        #self.M3.setInverted(True)
        self.right = wpilib.SpeedControllerGroup(self.M2,self.M3)

        # Drive setup
        self.drive = wpilib.drive.DifferentialDrive(self.left, self.right)
        self.drive.setMaxOutput(self.driveFactor)

        # Misc Setting
        self.stick = wpilib.Joystick(0)
        self.timer = wpilib.Timer()

        # E = Elevator
        self.E1 = wpilib.VictorSP(0) #This initializes the left elevator.
        self.E2 = wpilib.VictorSP(1) #This initializes the right elevator.
        # Shoulder
        self.S1 = wpilib.VictorSP(2) #This initializes the left shoulder.
        self.S2 = wpilib.VictorSP(3) #This initializes the right shoulder.
        
        #Servo
        self.SV1 = wpilib.Servo(4) #This initializes a servo.
        #self.SV2 = wpilib.Servo(5)
        #self.SV1.set(0.0)
        #self.SV2.set(0.0)
        
        #Gyro
        self.gyro = wpilib.ADXRS450_Gyro(0) #This initializes a gyro to detect the direction of the robot.
        self.gyro.reset() #This resets the gyro.
        
        
        
        
    



    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        #All possible autonomous routines in a sendable chooser
        #Each possibility has a list of items:
        #Example Start position 1 + scale: straight 3.5m turn 90 right forward 1.0m deliver cube
        self.timer.reset()
        self.timer.start()
        self.goldenArrowhead.set(True)
        #self.auto = self.sd.getNumber("auto",0) 
        #self.target = self.sd.getNumber("target",0) #Scale or Switch (value:1-switch or 2-scale)
        #self.startP = self.sd.getNumber("startP",0) #left-1 middle-2 right-3
        #self.colours = DriverStation.getInstance().getGameSpecificMessage()
        #self.ourSwitch = self.colours[0]
        #self.scale = self.colours[1]
        #self.theirSwitch = self.colours[2]
        '''
        self.EC1.setDistancePerPulse(1)
        self.EC2.setDistancePerPulse(1)
        self.EC3.setDistancePerPulse(1)
        self.EC4.setDistancePerPulse(1)
        '''
        '''
		#Determines autonomous modes
        if self.startP == 1:
            if self.target == 1:
                if self.ourSwitch == "L":
                    self.auto = 2
                else:
                    self.auto = 5
            elif self.target == 2:
                if self.scale == "L":
                    self.auto = 7
                else:
                    self.auto = 9
        if self.startP == 2:
            if self.target == 1:
                if self.ourSwitch == "L":
                    self.auto = 3
                else:
                    self.auto = 4
            elif self.target == 2:
                if self.scale == "L":
                    self.auto = 0
                else:
                    self.auto = 0
        if self.startP == 3:
            if self.target == 1:
                if self.ourSwitch == "L":
                    self.auto = 6
                else:
                    self.auto = 1
            elif self.target == 2:
                if self.scale == "L":
                    self.auto = 10
                else:
                    self.auto = 8
        self.auto = -1
        '''    
                
                
                
        #self.allianceColour = wpilib.DriverStation.getAlliance()
        #***************** GOLDEN ARROWHEAD = TRUE!!!!! *****************
        #self.auto = self.chooser.getSelected()
        '''
        self.cumulativeTime=0
        self.totalTime=0
        self.dataSet=[[-0.5,0,1,-1.0],[0.3,0.4,1,1.0],[-0.5,0,1,-1.0]]
        for i in self.dataSet:
            self.totalTime+=i[2]
        self.intervals = 0
        self.currentTime = 0
        for i in range(0,len(self.dataSet)):
            self.dataSet[i].append([self.currentTime,self.currentTime+self.dataSet[i][2]])
            self.currentTime+=self.dataSet[i][2]
        for i in self.dataSet:
            if i[3]==1.0:
                i.append("Forward")
            if i[3]==-1.0:
                i.append("Backward")
                
        self.timer.reset()
        self.timer.start()
        '''
        #self.EC1.reset()
        #self.EC2.reset()
        #self.EC1.setDistancePerPulse(0.01)        
        
            
    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        '''
        for i in self.dataSet:
            if i[4][0] < self.timer.get() and self.timer.get() <= i[4][1]:
                self.drive.arcadeDrive(i[0],i[1])
                self.SV1.set(i[3])
                self.sd.putValue("Camera",i[5])
            else:
                self.drive.arcadeDrive(0,0)
        '''       
        #Turning: clockwise-positive, counterclockwise - negative
        #Gyro: clockwise - positive; counterclockwise - negative
        #Place the robot backwards
        #Right -> Right Switch
        if self.timer.get() >= 0 and self.timer.get() <= 10:
            #self.M1.set(-0.5)
            #self.M0.set(-0.5)
            #self.M2.set(-0.5)
            #self.M3.set(-0.5)
            self.drive.arcadeDrive(1,0)
        '''
		if self.auto == 1:
            if self.autoState == 0:
                if self.gyro.getAngle() >= -14 and self.gyro.getAngle() <= 10: #Turn counterclockwise for 14 degrees. The value from the gyro will fluctuate.
                    self.drive.arcadeDrive(0.5,-0.7) 
                else:
                    self.autoState = 1
                    self.EC1.reset()
            if self.autoState == 1:
                if self.EC1.getDistance() <= 377 and self.EC1.getDistance() >= 0: #Go forward for 377 cm.
                    self.drive.arcadeDrive(0.6,0)
                else:
                    self.autoState = 2
            #This part makes the robot place the cube onto the switch or scale.
            if self.autoState == 2:
                if self.EC4.getDistance() <= 831 and self.EC4.getDistance() >= 0:  
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 3
            if self.autoState == 3:
                self.goldenArrowhead.set(False)
                self.autoState = 4
            if self.autoState == 4:
                if self.EC4.getDistance() >= 831 and self.EC4.getDistance() <= 887:
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 5
            if self.autoState == 5:
                if self.EC4.getDistance() >= 0 and self.EC4.getDistance() <= 900:
                    self.S1.set(0.25)
                    self.S2.set(0.25)
                else:
                    self.autoState = 6
            #Take arms back to rest position
        #Left -> Left Switch
        if self.auto == 2:
            if self.autoState == 0:
                if self.gyro.getAngle() >= -10 and self.gyro.getAngle() <= 9: 
                    self.drive.arcadeDrive(0.5,0.7)
                else:
                    self.autoState = 1
                    self.EC1.reset()
            if self.autoState == 1:
                if self.EC1.getDistance() <= 288 and self.EC1.getDistance() >= 0: #cm
                    self.drive.arcadeDrive(0.6,0)
                else:
                    self.autoState = 2
            if self.autoState == 2:
                if self.EC4.getDistance() <= 831 and self.EC4.getDistance() >= 0:  
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 3
            if self.autoState == 3:
                self.goldenArrowhead.set(False)
                self.autoState = 4
            if self.autoState == 4:
                if self.EC4.getDistance() >= 831 and self.EC4.getDistance() <= 887:
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 5
            if self.autoState == 5:
                if self.EC4.getDistance() >= 0 and self.EC4.getDistance() <= 900:
                    self.S1.set(0.25)
                    self.S2.set(0.25)
                else:
                    self.autoState = 6
            #Take arms back - set auto state to 0 (or go get another cube????)
        #Middle -> Left Switch  
        if self.auto == 3:
            if self.autoState == 0:
                if self.gyro.getAngle() >= -12 and self.gyro.getAngle() <= 10: 
                    self.drive.arcadeDrive(0.5,-0.7)
                else:
                    self.autoState = 1
                    self.EC1.reset()
            if self.autoState == 1:
                if self.EC1.getDistance() <= 291 and self.EC1.getDistance() >= 0: #458cm is the distance
                    self.drive.arcadeDrive(0.6,0)
                else:
                    self.autoState = 2
        '''
        '''
            DO NOT NEED TO TURN BACK TO VERTICAL!
            if self.autoState == 2:
                if self.gyro.getAngle() >= -37 and self.gyro.getAngle() <= 0:
                    self.drive.arcadeDrive(0.5,0.7)
                else:
                    self.autoState = 3
        '''
        '''
            if self.autoState == 2:
                if self.EC4.getDistance() <= 831 and self.EC4.getDistance() >= 0:  
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 3
            if self.autoState == 3:
                self.goldenArrowhead.set(False)
                self.autoState = 4
            if self.autoState == 4:
                if self.EC4.getDistance() >= 831 and self.EC4.getDistance() <= 887:
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 5
            if self.autoState == 5:
                if self.EC4.getDistance() >= 0 and self.EC4.getDistance() <= 900:
                    self.S1.set(0.25)
                    self.S2.set(0.25)
                else:
                    self.autoState = 6
            #Arms back....
            
            
        #Middle -> Right Switch
        if self.auto == 4:
            if self.autoState == 0:
                if self.gyro.getAngle() >= -10 and self.gyro.getAngle() <= 22:
                    self.drive.arcadeDrive(0.5,0.7)
                else:
                    self.autoState = 1
                    self.EC1.reset()
            if self.autoState == 1:
                if self.EC1.getDistance() <= 312 and self.EC1.getDistance() >= 0: #cm
                    self.drive.arcadeDrive(0.6,0)
                else:
                    self.autoState = 2
            if self.autoState == 2:
                if self.gyro.getAngle() >= -22 and self.gyro.getAngle() <= 10:
                    self.drive.arcadeDrive(0.5,-0.7)
                else:
                    self.autoState = 3
            if self.autoState == 3:
                if self.EC4.getDistance() <= 831 and self.EC4.getDistance() >= 0: #shoulder
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 4
            if self.autoState == 4:
                if self.EC4.getDistance() <= 831 and self.EC4.getDistance() >= 0:  
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 5
            if self.autoState == 5:
                self.goldenArrowhead.set(False)
                self.autoState = 6
            if self.autoState == 6:
                if self.EC4.getDistance() >= 831 and self.EC4.getDistance() <= 887:
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 7
            if self.autoState == 7:
                if self.EC4.getDistance() >= 0 and self.EC4.getDistance() <= 900:
                    self.S1.set(0.25)
                    self.S2.set(0.25)
                else:
                    self.autoState = 8
        
        #Left -> Right Switch
        if self.auto == 5:
            if self.autoState == 0:
                if self.gyro.getAngle() >= -10 and self.gyro.getAngle() <= 56:
                    self.drive.arcadeDrive(0.5,0.7)
                else:
                    self.autoState = 1
                    self.EC1.reset()
            if self.autoState == 1:
                if self.EC1.getDistance() <= 545 and self.EC1.getDistance() >= 0: #cm, not accurate
                    self.drive.arcadeDrive(0.6,0)
                else:
                    self.autoState = 2
            if self.autoState == 2:
                if self.gyro.getAngle() >= 0 and self.gyro.getAngle() <= 60:
                    self.drive.arcadeDrive(0.5,-0.7)
                else:
                    self.autoState = 3
                    self.EC1.reset()
            if self.autoState == 3:
                if self.EC1.getDistance() <= 61 and self.EC1.getDistance() >= 0:
                    self.drive.arcadeDrive(0.6,0)
                else:
                    self.autoState = 4
            if self.autoState == 4:
                if self.EC4.getDistance() <= 831 and self.EC4.getDistance() >= 0:  
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 5
            if self.autoState == 5:
                self.goldenArrowhead.set(False)
                self.autoState = 6
            if self.autoState == 6:
                if self.EC4.getDistance() >= 831 and self.EC4.getDistance() <= 887:
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 7
            if self.autoState == 7:
                if self.EC4.getDistance() >= 0 and self.EC4.getDistance() <= 900:
                    self.S1.set(0.25)
                    self.S2.set(0.25)
                else:
                    self.autoState = 8
        #Right -> Left Switch
        if self.auto == 6:
            if self.autoState == 0:
                if self.gyro.getAngle() >= -54 and self.gyro.getAngle() <= 10:
                    self.drive.arcadeDrive(0.5,-0.7)
                else:
                    self.autoState = 1
                    self.EC1.reset()
            if self.autoState == 1:
                if self.EC1.getDistance() <= 436 and self.EC1.getDistance() >= 0:
                    self.drive.arcadeDrive(0.6,0)
                else:
                    self.autoState = 2 
            if self.autoState == 2:
                if self.gyro.getAngle() >= -60 and self.gyro.getAngle() <= 0:
                    self.drive.arcadeDrive(0.5,0.7)
                else:
                    self.autoState = 3
                    self.EC1.reset()
            if self.autoState == 3:
                if self.EC1.getDistance() <= 61 and self.EC1.getDistance() >= 0:
                    self.drive.arcadeDrive(0.6,0)
                else:
                    self.autoState = 4
            if self.autoState == 4:
                if self.EC4.getDistance() <= 831 and self.EC4.getDistance() >= 0:  
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 5
            if self.autoState == 5:
                self.goldenArrowhead.set(False)
                self.autoState = 6
            if self.autoState == 6:
                if self.EC4.getDistance() >= 831 and self.EC4.getDistance() <= 887:
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 7
            if self.autoState == 7:
                if self.EC4.getDistance() >= 0 and self.EC4.getDistance() <= 900:
                    self.S1.set(0.25)
                    self.S2.set(0.25)
                else:
                    self.autoState = 8
        
        '''
        '''
		initial route
        if self.auto == 7:
            if self.autoState == 0: #Turn 5 degrees
                if self.gyro.getAngle() >= -5 and self.gyro.getAngle() <= 0:
                    self.drive.arcadeDrive(0.5,-0.7)
                else:
                    self.autoState = 1
                    self.EC1.reset()
            if self.autoState == 1: #Drive 4m
                if self.EC1.getDistance() <= 400 and self.EC1.getDistance() >= 0: #cm
                    self.drive.arcadeDrive(0.6,0)
                else:
                    self.autoState = 2
            if self.autoState == 2: #Turn back 5 degrees
                if self.gyro.getAngle() >= -5 and self.gyro.getAngle() <= 0:
                    self.drive.arcadeDrive(0.5,0.7)
                else:
                    self.autoState = 3
                    self.EC1.reset()
            if self.autoState == 3: #Drive 3.62m
                if self.EC1.getDistance() <= 362 and self.EC1.getDistance() >= 0: #cm
                    self.drive.arcadeDrive(0.6,0)
                else:
                    self.autoState = 4
            if self.autoState == 4: #Time to deliver cube - arms up
                if self.EC4.getDistance() <= 831 and self.EC4.getDistance() >= 0: #shoulder
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 5
            if self.autoState == 5: #Release!
                if self.EC4.getDistance() >= 831 and self.EC4.getDistance() <= 887:
                    self.goldenArrowhead.set(False)
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 6  #See you later
        '''
        '''
		#Left -> Left Scale
        if self.auto == 7:
            if self.autoState == 0: #Turn 5 degrees
                if self.EC1.getDistance() <= 488:
                    self.drive.arcadeDrive(0.6,0)
                else:
                    self.autoState = 1
                    self.EC1.reset()
            if self.autoState == 1: #Drive 4m
                if self.gyro.getAngle() >= -10 and self.gyro.getAngle() <= 28:
                    self.drive.arcadeDrive(0.5,0.7)
                else:
                    self.autoState = 2
                    self.EC1.reset()
            if self.autoState == 2: #Turn back 5 degrees
                if self.EC1.getDistance() <= 310 and self.EC1.getDistance() >= 0: #cm
                    self.drive.arcadeDrive(0.6,0)
                else:
                    self.autoState = 3
            if self.autoState == 3:
                if self.EC4.getDistance() <= 831 and self.EC4.getDistance() >= 0:  
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 4
            if self.autoState == 4:
                self.goldenArrowhead.set(False)
                self.autoState = 5
            if self.autoState == 5:
                if self.EC4.getDistance() >= 831 and self.EC4.getDistance() <= 887:
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 6
            if self.autoState == 6:
                if self.EC4.getDistance() >= 0 and self.EC4.getDistance() <= 900:
                    self.S1.set(0.25)
                    self.S2.set(0.25)
                else:
                    self.autoState = 7  #Arms Down, Go for next cube.....then...See you later
        #Right -> Right Scale
        if self.auto == 8:
            if self.autoState == 0: #Turn 5 degrees
                if self.EC1.getDistance() <= 488:
                    self.drive.arcadeDrive(0.6,0)
                else:
                    self.autoState = 1
                    self.EC1.reset()
            if self.autoState == 1: #Drive 4m
                if self.gyro.getAngle() >= -28 and self.gyro.getAngle() <= 10:
                    self.drive.arcadeDrive(0.5,-0.7)
                else:
                    self.autoState = 2
                    self.EC1.reset()
            if self.autoState == 2: #Turn back 5 degrees
                if self.EC1.getDistance() <= 310 and self.EC1.getDistance() >= 0: #cm
                    self.drive.arcadeDrive(0.6,0)
                else:
                    self.autoState = 3
            if self.autoState == 3:
                if self.EC4.getDistance() <= 831 and self.EC4.getDistance() >= 0:  
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 4
            if self.autoState == 4:
                self.goldenArrowhead.set(False)
                self.autoState = 5
            if self.autoState == 5:
                if self.EC4.getDistance() >= 831 and self.EC4.getDistance() <= 887:
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 6
            if self.autoState == 6:
                if self.EC4.getDistance() >= 0 and self.EC4.getDistance() <= 900:
                    self.S1.set(0.25)
                    self.S2.set(0.25)
                else:
                    self.autoState = 7  #See you later
        #left -> Right Scale
        if self.auto == 9:
            if self.autoState == 0:
                if self.EC1.getDistance() <= 589:
                    self.drive.arcadeDrive(0.6,0)
                else:
                    self.autoState = 1
                    self.EC1.reset()
            if self.autoState == 1:
                if self.gyro.getAngle() <= 90 and self.gyro.getAngle() >= -10:
                    self.drive.arcadeDrive(0.5,0.7)
                else:
                    self.autoState = 2
                    self.EC1.reset()
            if self.autoState == 2:
                if self.EC1.getDistance() <= 640 and self.EC1.getDistance() >= 0:
                    self.drive.arcadeDrive(0.6,0)
                else:
                    self.autoState = 3
                    self.EC1.reset()
            if self.autoState == 3:
                if self.gyro.getAngle() <= 95 and self.gyro.getAngle() >= 0:
                    self.drive.arcadeDrive(0.5,-0.7)
                else:
                    self.autoState = 4
                    self.EC1.reset()
            if self.autoState == 4:
                if self.EC1.getDistance() <= 174 and self.EC1.getDistance() >= 0:
                    self.drive.arcadeDrive(0.6,0)
                else:
                    self.autoState = 5
            if self.autoState == 5:
                if self.EC4.getDistance() <= 831 and self.EC4.getDistance() >= 0:  
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 6
            if self.autoState == 6:
                self.goldenArrowhead.set(False)
                self.autoState = 7
            if self.autoState == 7:
                if self.EC4.getDistance() >= 831 and self.EC4.getDistance() <= 887:
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 8
            if self.autoState == 8:
                if self.EC4.getDistance() >= 0 and self.EC4.getDistance() <= 900:
                    self.S1.set(0.25)
                    self.S2.set(0.25)
                else:
                    self.autoState = 9 #See you later

        #Right -> Left Scale
        if self.auto == 10:
            if self.autoState == 0:
                if self.EC1.getDistance() <= 589:
                    self.drive.arcadeDrive(0.6,0)
                else:
                    self.autoState = 1
                    self.EC1.reset()
            if self.autoState == 1:
                if self.gyro.getAngle() <= 10 and self.gyro.getAngle() >= -90:
                    self.drive.arcadeDrive(0.5,-0.7)
                else:
                    self.autoState = 2
                    self.EC1.reset()
            if self.autoState == 2:
                if self.EC1.getDistance() <= 640 and self.EC1.getDistance() >= 0:
                    self.drive.arcadeDrive(0.6,0)
                else:
                    self.autoState = 3
                    self.EC1.reset()
            if self.autoState == 3:
                if self.gyro.getAngle() <= 0 and self.gyro.getAngle() >= -95:
                    self.drive.arcadeDrive(0.5,0.7)
                else:
                    self.autoState = 4
                    self.EC1.reset()
            if self.autoState == 4:
                if self.EC1.getDistance() <= 174 and self.EC1.getDistance() >= 0:
                    self.drive.arcadeDrive(0.6,0)
                else:
                    self.autoState = 5
            if self.autoState == 5:
                if self.EC4.getDistance() <= 831 and self.EC4.getDistance() >= 0:  
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 6
            if self.autoState == 6:
                self.goldenArrowhead.set(False)
                self.autoState = 7
            if self.autoState == 7:
                if self.EC4.getDistance() >= 831 and self.EC4.getDistance() <= 887:
                    self.S1.set(-0.25)
                    self.S2.set(-0.25)
                else:
                    self.autoState = 8
            if self.autoState == 8:
                if self.EC4.getDistance() >= 0 and self.EC4.getDistance() <= 900:
                    self.S1.set(0.25)
                    self.S2.set(0.25)
                else:
                    self.autoState = 9 #See you later           
            '''            
                    
        self.sd.putValue('EC1',self.EC1.getDistance())
        self.sd.putValue('EC2',self.EC2.getDistance())
        self.sd.putValue('EC3',self.EC3.getDistance())
        self.sd.putValue('EC4',self.EC4.getDistance())
        #self.sd.putNumber('S1',self.S1)
        #self.sd.putNumber('S2',self.S2)
            
        #left -> Right Scale 
        #Right -> Left Scale
        #self.EC1.getRate() - Get the current rate of the encoder. Units are distance per second as scaled by the value from setDistancePerPulse().
        
    def teleopPeriodic(self):
        " ""This function is called periodically during operator control."""
	
        #Set the maximum output of the drive based on the left trigger:
        #self.drive.setMaxOutput(1.0-self.stick.getRawAxis(3))
        # Drive setting - use left stick for forward drive and right stick for backward drive
        #if self.stick.getRawAxis(4)==0 and self.stick.getRawAxis(5)==0:
        self.drive.arcadeDrive(-1*self.stick.getRawAxis(0), self.stick.getRawAxis(1))
        #if self.stick.getRawAxis(0)==0 and self.stick.getRawAxis(1)==0:
        #    self.drive.arcadeDrive(-1*self.stick.getRawAxis(4),self.stick.getRawAxis(5))

        # Elevator
        # 2018-2-16 Warning! The Switch number should be modified accroding to the robot! - Fixed
        '''
        WITHOUT STATE MACHINES
        #ELevator
        if self.stick.getRawButton(1) == True: 
            self.E1.set(0.5)
            self.E2.set(-0.5)
        elif self.stick.getRawButton(2) == True: 
            self.E1.set(-0.5)
            self.E2.set(0.5)
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
        '''

        #Pneumatics
	#Powercube collector - "Golden Arrowhead"
        #if self.stick.getRawButton(1) == True:
        #    self.prepareCubeFlag = 1
        #    self.pstate = 1
        #    self.EC3.reset()
        #if self.prepareCubeFlag > 0:
        #    self.prepareGrabCube()
        #if self.stick.getRawButton(2) == True:
        #    self.grabCubeFlag = 1
        #    self.gstate = 1  
        #    self.EC3.reset()
        #if self.grabCubeFlag > 0:
        #    self.grabCube()
        #if self.stick.getRawButton(3) == True:
        #    self.deliverCubeFlag = 1
        #    self.dstate = 1
        #    self.EC4.reset()
        #if self.deliverCubeFlag > 0:   
        #    self.deliverCube()
            
        #if self.stick.getRawButton(5)==True:
        #    self.goldenArrowhead.set(True)
        #elif self.stick.getRawButton(6)==True:
        #    self.goldenArrowhead.set(False)
        #Moving up the elevators
        #Shift Gears
        '''
        if self.stick.getRawButton(7)==True:
            self.leftGearShift.set(True)
            self.rightGearShift.set(True)
        elif self.stick.getRawButton(8)==True:
            self.leftGearShift.set(False)
            self.rightGearShift.set(False)
        '''
        #Moves up the arm to release the cube
        if self.stick.getRawButton(3)==True: # and self.EC3.getDistance() >= -100 and self.EC3.getDistance() <= 100:
            self.S1.set(-0.35)
            self.S2.set(-0.35)
            #Triggers for the arm
            self.S1.set(-(self.stick.getRawAxis(2)*0.75+0.25))
            self.S2.set(-(self.stick.getRawAxis(2)*0.75+0.25))
        #Moves down the arm
        elif self.stick.getRawButton(4)==True: # and self.EC3.getDistance() >= -100 and self.EC3.getDistance() <= 100:
            self.S1.set(0.35)
            self.S2.set(0.35)
            #Triggers for the arm
            #self.S1.set(self.stick.getRawAxis(2)*0.75+0.25)
            #self.S2.set(self.stick.getRawAxis(2)*0.75+0.25)
        #Climbing - moving down the elevators
        if self.stick.getRawButton(1) == True:
            self.E1.set(-0.8)
            self.E2.set(0.8)
        if self.stick.getRawButton(2) == True:
            self.E1.set(0.8)
            self.E2.set(-0.8)
            
        #Camera Point Front:
        if self.stick.getPOV()==0:
            self.SV1.set(1.0)
            self.camera='Forwards'
        #Camera Point Back:
        if self.stick.getPOV()==180:
            self.SV1.set(-1.0)
            self.camera='Backwards'
        #Adjust left elevators
        if self.stick.getPOV()==90:
            self.E1.set(-0.3)
        #Adjust right elevators
        if self.stick.getPOV()==270:
            self.E2.set(0.3)
            
        
        
        
        #Dashboard
        #self.sd.putNumber('Speed', 0.5)
        self.sd.putNumber('Gyro',self.gyro.getAngle())
        #self.sd.putValue("Camera", self.camera)
        #self.sd.putValue("SW1", self.SW1.get())
        #self.sd.putValue("SW0", self.SW0.get())
        self.sd.putNumber('EC1',self.EC1.getDistance())
        self.sd.putNumber('EC2',self.EC2.getDistance())
        self.sd.putNumber('EC3',self.EC3.getDistance())
        self.sd.putNumber('EC4',self.EC4.getDistance())
        #self.sd.putNumber('S1',self.S1)
        #self.sd.putNumber('S2',self.S2)
        #self.sd.putNumber('E1',self.E1)
        #self.sd.putNumber('E2',self.E2)
        self.sd.putNumber('SV1',self.SV1.get())
        #self.sd.putNumber('SV2',self.SV2.get())

        
    def speedUpArm(self):
        self.S1.set(self.S1.get()*6/10+0.4) 
        self.S2.set(self.S2.get()*6/10+0.4)
        
    def prepareGrabCube(self):
    #(1)Check that the lower elevator switch is on - elevator at bottom
	#(2)If not, move elevator to bottom (and arms to bottom)
        if self.pstate == 1:
            if self.EC3.getDistance() <= 30720:
                self.E1.set(0.5)
                self.E2.set(-0.5)
            self.pstate = 2
        if self.pstate == 2:
            self.E1.set(0)
            self.E2.set(0)
            self.prepareCubeFlag = 0
            
    def grabCube(self):
    #(1)Grab cube
    #(2) Move cube up until it hits the top (or part way up????)
        if self.gstate == 1:
            self.goldenArrowhead.set(True)
            self.gstate = 2
            #Grabs the cube(not sure it is True or False)
        if self.gstate == 2:
            if self.EC3.getDistance() >= -30720 and self.EC3.getDistance() <= 0:
                self.E1.set(-0.5)
                self.E2.set(0.5)
            self.gstate = 3
        if self.gstate == 3:
            self.E1.set(0)
            self.E2.set(0)
            self.grabCubeFlag = 0
    
    def deliverCube(self):
        if self.dstate == 1:
            if self.EC4.getDistance() <= 5000:#larger not precise
                self.S1.set(-0.25)
                self.S2.set(-0.25)
            self.dstate = 2
        if self.dstate == 2:
            self.goldenArrowhead.set(False)
            self.dstate = 3
        if self.dstate == 3:
            if self.EC4.getDistance() >= 5000 and self.EC4.getDistance() <= 6000:
                self.S1.set(-0.25)
                self.S2.set(-0.25)
            self.dstate = 4
        if self.dstate == 4:
            if self.EC4.getDistance() >= 0 and self.EC4.getDistance() <= 6000:
                self.S1.set(0.25)
                self.S2.set(0.25)
            self.deliverCubeFlag=0
            
    
if __name__ == "__main__":
    wpilib.run(MyRobot)

