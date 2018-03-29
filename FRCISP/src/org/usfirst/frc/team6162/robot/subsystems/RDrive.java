package org.usfirst.frc.team6162.robot.subsystems;

import com.ctre.phoenix.motorcontrol.can.WPI_TalonSRX;
import edu.wpi.first.wpilibj.drive.*;
import edu.wpi.first.wpilibj.SpeedControllerGroup;
import edu.wpi.first.wpilibj.command.Subsystem;
import edu.wpi.first.wpilibj.VictorSP;

/**
 *
 */
public class RDrive extends Subsystem {

    // Initialize motors (competition robot)
	//private final WPI_TalonSRX rightFront = new WPI_TalonSRX(1);
	//private final WPI_TalonSRX rightBack = new WPI_TalonSRX(2);
	//private final WPI_TalonSRX leftFront = new WPI_TalonSRX(3);
	//private final WPI_TalonSRX leftBack = new WPI_TalonSRX(4);	
	
	//Initialize motors (test robot)
	private final VictorSP rightFront = new VictorSP(0);
	private final VictorSP rightBack = new VictorSP(1);
	private final VictorSP leftFront = new VictorSP(2);
	private final VictorSP leftBack = new VictorSP(3);	

	
	
	//SpeedControllerGroup for arcade drive
	SpeedControllerGroup motorGroupLeft = new SpeedControllerGroup(leftFront, leftBack);
	SpeedControllerGroup motorGroupRight = new SpeedControllerGroup(rightFront, rightBack);
	DifferentialDrive motorDiffDriveMain =  new DifferentialDrive(motorGroupLeft, motorGroupRight);
	
    public void initDefaultCommand() {
        // Set the default command for a subsystem here.
        //setDefaultCommand(new MySpecialCommand());
    }
    
    public void driveArcade(double xSpeed, double zRotation) {
    	motorDiffDriveMain.arcadeDrive(xSpeed, zRotation);
    }
    
    public void driveDirect(double left, double right) {
    	runLeft(left);
    	runRight(right);
    }
    
    public void stop() {
    	leftFront.stopMotor();
    	leftBack.stopMotor();
    	rightFront.stopMotor();
    	rightBack.stopMotor();
    }
    
    private void runLeft(double input) { 
    	leftFront.set(input);
    	leftBack.set(input);
    }
    
    private void runRight(double input) {
    	rightFront.set(input);
    	rightBack.set(input);
    }
}
