package org.usfirst.frc.team6162.robot.commands;

import org.usfirst.frc.team6162.robot.Robot;

import edu.wpi.first.wpilibj.command.Command;

/**
 *
 */
public class deliverCube extends Command {

    public deliverCube() {
        // Use requires() here to declare subsystem dependencies
        // eg. requires(chassis);
    	super("deliverCube");
    	requires(Robot.rarms);
    }

    // Called just before this Command runs the first time
    protected void initialize() {
    }

    // Called repeatedly when this Command is scheduled to run
    protected void execute() {
    	if (Robot.rdrive.EC1.getDistance() <= 5000 && Robot.rdrive.EC1.getDistance() >= 0) {
    		Robot.rarms.flipUp();
    	}
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
