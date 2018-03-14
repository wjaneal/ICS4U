# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 12:53:59 2018
@author: fy

Name of group: First Triumvirate
Group members: Charlotte, Emma and Khan
Name of Project: ICS4U ISP - FRC(First Robotic Competition) Project
Project Purpose: To make our robot thrive in the competitions!
Details of Project (20-30 details that thoroughly describe the aims of the planned project):
        √i.to make it able to grab cubes, (DOING)to travel as we wish, and to climb up to the tower;
       √ii. to make the data visible;
(DOING) iii. to make robot take actions according to the color being recognised.

Project Management Technique to be used:
Agile - Planning and test together quickly throughout all the sessions involved
(figure out the requirements of the match→give them definitions→start planning→start designing→implement/test→release→repair if needed).
P.S. This is an iterative flow;Phases can overlap or repeat as needed.

Content of code:
√①Framework - construction of robot.py (a base file which allows our robot to do whatever we want);
                Organization of names of variables (will be listed below)
（DOING)②GUI - interface of displaying the data which we wre using in order to determine what the next action the robot needs to take
√③Encoder - detection of distance and time taken by the robot
√④Motor - an device which supports the movement of the robot
√⑤Gyro - determine the direction of the robot
√⑥State Machine - a series of movement provided for saving time and safety(rules in matches) concerns
√⑦Pneumatic Systems - a controller of the arms for opening and closing(grabbing or releasing an cube)
√⑧Switches - spots of stopping the elevator
√(WILL USE LEO'S SOFTWARE FOR THE MATCHES)⑨Color Recognition System - e.g. our robot will grab the cubes if the robot sees yellow

Variables:
M0;M1 - Motors on the left side (control the wheels on the left side)
left - MotorGroup for the left side(gather M0 & M1)
M2;M3 - Motors on the right side (control the wheels on the right side)
right - MotorGroup for the right side (gather M2 & M3)
sd - NetworkTable (display the data of all variables)
driveFactor - adjust controller responsiveness
EC1;EC2 - detect distance of robot travelled (Encoders on the base)
EC3;EC4 - (determine the time when the shoulders should be released)
goldenArrowhead - center of Pneumatic system (make arms open or close)
E1;E2 - Motors on the elevator (make the shoulders go up or down)
S1;S2 - Motors on the shoulders (flip the shoulder up or down)
SV1 - Servo on the Camera(make it turned)
gyro - detect the direction of robot travelled
auto - different choices of autonomous session
SW0 - Switch at the spot where the elevator should be stopped (lower)
SW1 - Switch at the spot where the elevator should be stopped (higher)

Timeline:
The days before Mar.7 - We started designing the GUI(determining which data we should display);
                        We finished coding the Gyro;
                        We finished coding the motor;
                        We finished coding the Pneumatic system;
                        We assigned all the variables of coding;
                        We finished coding the switches... etc.
                        
Mar.7 - We coded and tested the code about Encoder as well as state machines and they worked;
        We made a list of all the variables.

The days between Mar.8 and Mar.12 - Finished coding all the sample options in the AutonomousPeriodic;
                                    Started coding reset function(only for testing);

Mar.12 - Checked the codes and tested the buttons for periodic - they worked;
         Started coding vedio processing;
        
Mar.13 - Started making a brand new GUI (formal version for competitions);
         Kept calculating data for the code of autonomousperodic;
         Stopped coding the reset function because we found out that we do not actually need it;
         
Mar.14 - Testing Leo's video processing software;

"""

