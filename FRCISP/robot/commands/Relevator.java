package org.usfirst.frc.team6162.robot.commands;

import org.usfirst.frc.team6162.robot.subsystems.RDrive;
import org.usfirst.frc.team6162.robot.subsystems.Elevator;

import edu.wpi.first.wpilibj.command.Command;



/**
 *
 */
public class Relevator extends Command {
	//Elevator E = new Elevator();	

    // Called just before this Command runs the first time
    protected void initialize() {
    	
    }

    // Called repeatedly when this Command is scheduled to run
    protected void execute() {
    	/*
    	if(controller.getAButton()) { //Button 1
		E.moveUp();
		}
    	else if (controller.getBButton()) { //Button 2
		E.moveDown();
		}
    	else {
			E.stopE();
    }
    */
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
