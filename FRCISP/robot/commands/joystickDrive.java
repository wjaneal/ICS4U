package org.usfirst.frc.team6162.robot.commands;

import org.usfirst.frc.team6162.robot.Robot;
import org.usfirst.frc.team6162.robot.subsystems.RDrive;
import org.usfirst.frc.team6162.robot.subsystems.Arms;
import edu.wpi.first.wpilibj.command.Command;


/**
 *
 */
public class joystickDrive extends Command {
	//RDrive drive = new RDrive();	
    public joystickDrive() {
        // Use requires() here to declare subsystem dependencies
        // eg. requires(chassis);
    	//requires(Drive);
    	super("joystickDrive");
    	requires(Robot.rdrive);
    	
    	
    }

    // Called just before this Command runs the first time
    protected void initialize() {
    	//Robot.rdrive.move();
    	Robot.rdrive.EC1.reset();
    //Robot.rdrive.gyro.calibrate();
    //	Robot.rdrive.gyro.setSensitivity(0.007);
    	//Robot.rdrive.gyro.reset();
    }

    // Called repeatedly when this Command is scheduled to run
    public void execute() {
    	//drive.driveArcade(1,1);
    	Robot.rdrive.EncoderDrive();
    //	Robot.rdrive.gyroDrive();
    }

    // Make this return true when this Command no longer needs to run execute()
    protected boolean isFinished() {
        return false;
    }

    // Called once after isFinished returns true
    protected void end() {
    }

    // Called when another command which requires one or more of the same
    // subsystems is scheduled to run
    protected void interrupted() {
    }
}
