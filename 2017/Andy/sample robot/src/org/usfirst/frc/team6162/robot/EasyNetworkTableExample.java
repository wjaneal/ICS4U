package org.usfirst.frc.team6162.robot;

import org.usfirst.frc.team6162.robot.Robot;

import edu.wpi.first.wpilibj.SampleRobot;
import edu.wpi.first.wpilibj.Timer;
import edu.wpi.first.wpilibj.networktables.NetworkTable;

public class EasyNetworkTableExample extends SampleRobot {
		NetworkTable table;
		
		
		public void robotInit(){
			table = NetworkTable.getTable("datatable");
		}
		
		public void autonomous(){
			
		}
		
		public void operatorControl(){
            double x=0;
            double y= 0;
            while(isOperatorControl()&&isEnabled()){
            	Timer.delay(0.25);
            	table.putNumber("x", x);
            	table.putNumber("y", y);
            	x+=0.5;
            	y+=1.0;
            }
		}
}
