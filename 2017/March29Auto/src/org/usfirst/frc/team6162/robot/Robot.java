package org.usfirst.frc.team6162.robot;

import org.opencv.core.Rect;
import org.opencv.imgproc.Imgproc;
import org.usfirst.frc.team6162.robot.GripPipeline;

import edu.wpi.first.wpilibj.RobotDrive;
import edu.wpi.first.wpilibj.SPI;
import edu.wpi.first.wpilibj.SampleRobot;
import edu.wpi.first.wpilibj.SpeedController;
import edu.wpi.first.wpilibj.Talon;
import edu.wpi.first.wpilibj.Joystick;
import edu.wpi.first.wpilibj.Preferences;
import edu.wpi.first.wpilibj.Timer;
import edu.wpi.first.wpilibj.interfaces.Gyro;
import edu.wpi.first.wpilibj.smartdashboard.SendableChooser;
import edu.wpi.first.wpilibj.smartdashboard.SmartDashboard;
import edu.wpi.first.wpilibj.vision.VisionPipeline;
import edu.wpi.first.wpilibj.vision.VisionThread;
import edu.wpi.first.wpilibj.AnalogGyro;
import edu.wpi.first.wpilibj.CameraServer;
import edu.wpi.first.wpilibj.IterativeRobot;
import edu.wpi.first.wpilibj.networktables.NetworkTable;

import org.opencv.core.Rect;
import org.opencv.imgproc.Imgproc;

import edu.wpi.cscore.UsbCamera;
import edu.wpi.first.wpilibj.ADXRS450_Gyro;
import edu.wpi.first.wpilibj.SPI.*;
import edu.wpi.first.wpilibj.smartdashboard.SmartDashboard;
/**
 * The VM is configured to automatically run this class, and to call the
 * functions corresponding to each mode, as described in the IterativeRobot
 * documentation. If you change the name of this class or the package after
 * creating this project, you must also update the manifest file in the resource
 * directory.
 */
public class Robot extends IterativeRobot {
	final String defaultAuto = "Default";
	final String customAuto = "My Auto";
	String autoSelected;
	SendableChooser<String> chooser = new SendableChooser<>();
	NetworkTable table;
	RobotDrive myRobot = new RobotDrive(0,1,2,3);
	GripPipeline GP = new GripPipeline();
	Joystick XboxController = new Joystick(0);

	private static final int IMG_WIDTH = 320;
	private static final int IMG_HEIGHT = 240;
	private VisionThread visionThread;
	private double centerX0 = 0.0;
	private double centerX1 = 0.0;
	private double centerY = 0.0;
	private double size0 = 0.0;
	private double size1 = 0.0;
	private double rw=30;
	private double rh=40;
	private double sizeMinimum = 16;
	private final Object imgLock = new Object();
	private enum Stage {stage1, stage2, stage3, stage4};
	public class Stages{
		Stage stage;
		
		public Stages(Stage s){
			this.stage = s;
		}
		
		
	}
	private Stages s = new Stages(Stage.stage1);	
	
	//private static final double kVoltsPerDegreePerSecond=0.0128;
	private SpeedController BallCollector = new Talon(4);
	private SpeedController Shooter = new Talon(6);
	private SpeedController Door = new Talon(7);
	private ADXRS450_Gyro gyro = new ADXRS450_Gyro(SPI.Port.kOnboardCS0);  		
	double angle; // get current heading
    double rate;//get rate of rotation
	
    
	Preferences prefs;
	
	double armUpPosition;
	double armDownPosition;
	/**
	 * This function is run when the robot is first started up and should be
	 * used for any initialization code.
	 */
	@Override
	public void robotInit() {
		chooser.addDefault("Default Auto", defaultAuto);
		chooser.addObject("My Auto", customAuto);
		SmartDashboard.putData("Auto choices", chooser);
	    UsbCamera camera = CameraServer.getInstance().startAutomaticCapture();
	    camera.setResolution(IMG_WIDTH, IMG_HEIGHT);
	    
	    visionThread = new VisionThread(camera, new GripPipeline(), pipeline -> {
	        if (!pipeline.filterContoursOutput().isEmpty()) {
	            Rect r0 = Imgproc.boundingRect(pipeline.filterContoursOutput().get(0));
	            Rect r1 = Imgproc.boundingRect(pipeline.filterContoursOutput().get(1));
	            synchronized (imgLock) {
	                centerX0 = r0.x + (r0.width / 2);
	                centerX1 = r1.x + (r1.width / 2);
	                size0 = r0.width;
	                size1 = r1.width;
	            }
	        }
	    });
	    visionThread.start();
	    
	}

	/**
	 * This autonomous (along with the chooser code above) shows how to select
	 * between different autonomous modes using the dashboard. The sendable
	 * chooser code works with the Java SmartDashboard. If you prefer the
	 * LabVIEW Dashboard, remove all of the chooser code and uncomment the
	 * getString line to get the auto name from the text box below the Gyro
	 *
	 * You can add additional auto modes by adding additional comparisons to the
	 * switch structure below with additional strings. If using the
	 * SendableChooser make sure to add them to the chooser code above as well.
	 */
	@Override
	public void autonomousInit() {
		autoSelected = chooser.getSelected();
		// autoSelected = SmartDashboard.getString("Auto Selector",
		// defaultAuto);
		System.out.println("Auto selected: " + autoSelected);
		s.stage = Stage.stage1;
	  //visionThread = new VisionThread(camera, new GripPipeline(), pipeline );  

	}

	/**
	 * This function is called periodically during autonomous
	 */
	@Override
	public void autonomousPeriodic() {
		double centerX;
		synchronized (imgLock) {
			centerX0 = this.centerX0;
			centerX1 = this.centerX1;
			size0 = this.size0;
			size1 = this.size1;
		}
		switch (s.stage) {
		//Stage 1 - Move until size0 and size1 are the correct size
		case stage1:
			double turn = centerX0 - (IMG_WIDTH / 2);
			SmartDashboard.putNumber("centerX0", centerX0);
			myRobot.drive(-0.35, -turn * 0.001);	
			if(size0>sizeMinimum || size1>sizeMinimum){
				s.stage = Stage.stage2;
			}
			break;
			
		//Stage 2 - Turn 90 degrees left
		case stage2:
			myRobot.drive(0.27,1);
			Timer.delay(0.80);
			s.stage=Stage.stage3;
			break;
		//Stage 3 - Move until size0 and size1 are the correct size
		case stage3:
		/*	turn = centerX0 - (IMG_WIDTH / 2);
			SmartDashboard.putNumber("centerX0", centerX0);
			myRobot.arcadeDrive(-0.6, turn * 0.005);	
			if(size0>sizeMinimum || size1<sizeMinimum){
				s.stage = Stage.stage4;
			}
			*/
			s.stage=Stage.stage4;
			break;
		case stage4:
			myRobot.arcadeDrive(0,0);
			break;
		}
		
		
	}

	/**
	 * This function is called periodically during operator control
	 */
	@Override
	public void teleopPeriodic() {
		double centerX;
		//synchronized (imgLock) {
			centerX0 = this.centerX0;
			centerX1 = this.centerX1;
			size0 = this.size0;
			size1 = this.size1;	
	//	}
		double turn = centerX0 - (IMG_WIDTH / 2);
		SmartDashboard.putNumber("centerX0", centerX0);
		SmartDashboard.putNumber("centerX1", centerX1);
		SmartDashboard.putNumber("Size0", size0);
		SmartDashboard.putNumber("Size1", size1);
		SmartDashboard.putNumber("Turn", turn);
		myRobot.arcadeDrive(XboxController);
		Timer.delay(0.01);
		if(XboxController.getRawAxis(4)!=0){
			BallCollector.set(XboxController.getRawAxis(4));
		}
		
	}

	/**
	 * This function is called periodically during test mode
	 */
	@Override
	public void testPeriodic() {
	}
}

