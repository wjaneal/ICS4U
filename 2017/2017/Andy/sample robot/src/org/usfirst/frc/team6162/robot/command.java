package org.usfirst.frc.team6162.robot;

import edu.wpi.first.wpilibj.Timer;

public class command extends Robot {
	
	public void SetAngle(double current, double desired){
		
		if(current<desired){
			myRobot.drive(0.1,current*0.1);
			Timer.delay(0.004);
		}else if(current>desired){
			myRobot.drive(0.1, current*-0.1);
			Timer.delay(0.004);
		}
	}
	
	
}
