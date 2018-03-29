package org.usfirst.frc.team6162.robot.subsystems;

import edu.wpi.first.wpilibj.VictorSP;
import edu.wpi.first.wpilibj.command.Subsystem;


/**
 *
 */
public class Elevator extends Subsystem {
	//Initialize motors for the elevator (competition robot)
	private final VictorSP E1 = new VictorSP(0);
	private final VictorSP E2 = new VictorSP(1);
	
    // Put methods for controlling this subsystem
    // here. Call these from Commands.

    public void initDefaultCommand() {
        // Set the default command for a subsystem here.
        //setDefaultCommand(new MySpecialCommand());
    }
    public void moveUp() {
    	E1.set(-0.6);
    	E2.set(0.6);
    }
    	public void moveDown() {
    	E1.set(0.6);
    E2.set(-0.6);
    	}
    	public void stopE(){
    	E1.set(0);
    	E2.set(0);
    	}
    	
}

