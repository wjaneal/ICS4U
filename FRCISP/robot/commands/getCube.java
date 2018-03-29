package org.usfirst.frc.team6162.robot.commands;

import org.usfirst.frc.team6162.robot.Robot;

import edu.wpi.first.wpilibj.command.Command;

/**
 *
 */
public class getCube extends Command {

    public getCube() {
        // Use requires() here to declare subsystem dependencies
        // eg. requires(chassis);
    	super("getCube");
    	requires(Robot.elevator);
    	requires(Robot.rarms);
    }

    // Called just before this Command runs the first time
    protected void initialize() {
    	Robot.rarms.Close();
    }

    // Called repeatedly when this Command is scheduled to run
    protected void execute() {
    
    	Robot.elevator.moveUp();
    }

    // Make this return true when this Command no longer needs to run execute()
    protected boolean isFinished() {
    	if (Robot.rdrive.EC1.getDistance() <= 5000 && Robot.rdrive.EC1.getDistance() >=0) {
    		return false;
    	}
    	else {
    		 return true;
    	}
       
    }

    // Called once after isFinished returns true
    protected void end() {
    	Robot.elevator.stopE();
    }

    // Called when another command which requires one or more of the same
    // subsystems is scheduled to run
    protected void interrupted() {
    }
}
