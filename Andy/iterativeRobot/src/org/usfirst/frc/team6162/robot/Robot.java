package org.usfirst.frc.team6162.robot;

import org.opencv.core.Rect;
import org.opencv.imgproc.Imgproc;

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
	Joystick XboxController = new Joystick(0);

	private static final int IMG_WIDTH = 320;
	private static final int IMG_HEIGHT = 240;
	private VisionThread visionThread;
	private double centerX = 0.0;
	private double centerY = 0.0;
	private double rw=30;
	private double rh=40;
	private final Object imgLock = new Object();
	
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
	            Rect r = Imgproc.boundingRect(pipeline.filterContoursOutput().get(0));
	            synchronized (imgLock) {
	                centerX = r.x + (r.width / 2);
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

	  //visionThread = new VisionThread(camera, new GripPipeline(), pipeline );  

	}

	/**
	 * This function is called periodically during autonomous
	 */
	@Override
	public void autonomousPeriodic() {
		double centerX;
		synchronized (imgLock) {
			centerX = this.centerX;
		}
		double turn = centerX - (IMG_WIDTH / 2);
		SmartDashboard.putNumber("centerX", centerX);
		myRobot.arcadeDrive(-0.6, turn * 0.005);
		switch (autoSelected) {
		case customAuto:
			
			// Put custom auto code here
			break;
		case defaultAuto:
		default:
			// Put default auto code here
			myRobot.arcadeDrive(0.6,0.0);
			Timer.delay(0.2);
			myRobot.arcadeDrive(0.4,0.4);
			Timer.delay(0.2);
			break;
		}
	}

	/**
	 * This function is called periodically during operator control
	 */
	@Override
	public void teleopPeriodic() {
		double centerX;
		synchronized (imgLock) {
			centerX = this.centerX;
		}
		double turn = centerX - (IMG_WIDTH / 2);
		SmartDashboard.putNumber("centerX", centerX);
		myRobot.arcadeDrive(XboxController);
		Timer.delay(0.2);
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

