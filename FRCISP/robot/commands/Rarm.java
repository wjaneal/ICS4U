package org.usfirst.frc.team6162.robot.commands;

import org.usfirst.frc.team6162.robot.subsystems.RDrive;
import org.usfirst.frc.team6162.robot.subsystems.Arms;

import edu.wpi.first.wpilibj.command.Command;



/**
 *
 */
public class Rarm extends Command {
	//Arms arm = new Arms();	
    

    // Called just before this Command runs the first time
    protected void initialize() {
    	
    }

    // Called repeatedly when this Command is scheduled to run
    protected void execute() {
    	/*
    	if(controller.getXButton()) { //Button 3
			arm.flipDown();
		}else if(controller.getYButton()) { //Button 4
			arm.flipUp();
		}else {
			arm.stopArm();
	if(controller.getRawButton(5)) { 
			arm.open();
		}else if(controller.getRawButton(6)) {
			arm.close();	
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
