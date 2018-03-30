package org.usfirst.frc.team6162.robot.commands;

import org.usfirst.frc.team6162.robot.Robot;

import edu.wpi.first.wpilibj.command.Command;

/**
 *
 */
public class prepareGetCube extends Command {

    public prepareGetCube() {
        // Use requires() here to declare subsystem dependencies
        // eg. requires(chassis);
    	super("prepareGetCube");
    requires(Robot.elevator);
    requires(Robot.rdrive);
    }

    // Called just before this Command runs the first time
    protected void initialize() {
    	Robot.rdrive.EC1.reset();
    }

    // Called repeatedly when this Command is scheduled to run
    protected void execute() {
    	Robot.rdrive.EncoderDrive();
    	
    	}

    // Make this return true when this Command no longer needs to run execute()
    protected boolean isFinished() {
    	if (Robot.rdrive.EC1.getDistance() >= 2000){
    		return true;
    	}
    	else {
    		return false;
    	}
    		
  
  
       
    }

    // Called once after isFinished returns true
    protected void end() {
    	Robot.elevator.servo1.set(0.5);
    }

    // Called when another command which requires one or more of the same
    // subsystems is scheduled to run
    protected void interrupted() {
    }
}
