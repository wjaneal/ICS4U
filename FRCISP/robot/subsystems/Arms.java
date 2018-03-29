package org.usfirst.frc.team6162.robot.subsystems;

import org.usfirst.frc.team6162.robot.Robot;

import edu.wpi.first.wpilibj.Solenoid;
import edu.wpi.first.wpilibj.VictorSP;
import edu.wpi.first.wpilibj.command.Subsystem;

/**
 *
 */
public class Arms extends Subsystem {
	//Initialize motors for the arm (competition robot)
	private final VictorSP S1 = new VictorSP(2);
	private final VictorSP S2 = new VictorSP(3);
	
	//Initialize goldenArrowHead
	private final Solenoid gAH = new Solenoid(0);
    // Put methods for controlling this subsystem
    // here. Call these from Commands.

    public void initDefaultCommand() {
        // Set the default command for a subsystem here.
        //setDefaultCommand(new MySpecialCommand());
    }
    public void flipUp() {
    	S1.set(0.6);
    	S2.set(0.6);
    }
    public void flipDown() {
    	S1.set(-0.6);
    	S2.set(-0.6);
    }
    public void stopArm(){
    S1.set(0);
    S2.set(0);
    }
    public void Open(){
    gAH.set(false);
    }
    public void Close(){
    gAH.set(true);
    }
    
    
}

