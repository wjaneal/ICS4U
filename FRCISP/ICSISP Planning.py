# -*- coding: utf-8 -*-
"""
Created on Mon Mar 5 12:53:59 2018
@author: Charlotte, Emma, and Khan

Name of group: First Triumvirate
Group members: Charlotte, Emma and Khan
Name of Project: ICS4U ISP - FRC(FIRST Robotics Competition) Project
Project Purpose: To make our robot thrive in the competitions!
Details of Project (20-30 details that thoroughly describe the aims of the planned project):
        √i.to make it able to grab cubes, (DOING) to travel as we wish, and to climb up to the tower;
       √ii. to display the data on the dashboard;
(DOING) iii. to make the robot move according to alliance color in autonomous session

Project Management Technique to be used:
Agile - For each part of our project, team members will plan and test together quickly.
(Flow: figure out the requirements of the match → give them definitions → start planning → start designing → implement/test→ release → repair if needed).
P.S. This is an iterative flow; Phases can overlap or repeat as needed.

Content of code:
√①Framework - Construction of robot.py (a base file which allows our robot to do whatever we want);
            - Organization of names of variables (will be listed below)
（DOING)②GUI - graphic user interface which displays the data used in order to determine the next action of the robot
√③Encoder - Detects of distance the robot has travelled
√④Motor - A device which supports the movement of the robot
√⑤Gyro - Determines the direction of the robot by using angles
√⑥State Machines - a series of movements which can save time and solve safety concerns (according to rules in matches) 
√⑦Pneumatic Systems - a controller of the arms for opening and closing (grabbing or releasing an cube)
√⑧Switches - Spots where elevators can be stopped.
√(WILL USE LEO'S SOFTWARE FOR THE MATCHES)⑨Color Recognition System - e.g. Our robot will grab the cubes if the robot sees yellow color.

Variables:
M0;M1 - Motors on the left side (to control the wheels on the left side)
left - MotorGroup for the left side(gathers M0 & M1)
M2;M3 - Motors on the right side (to control the wheels on the right side)
right - MotorGroup for the right side (gathers M2 & M3)
sd - NetworkTable (communication between our robot and the dashboard to display the data being used)
driveFactor - To adjust controller responsiveness
EC1;EC2 - To detect distance the robot has travelled (Encoders on the base)
EC3 - To detect the distance the elevator has moved
EC4 - To detect the angle the shoulders are at
goldenArrowhead - belongs to the Pneumatic system (to make arms open or close)
E1;E2 - Motors on the elevator (to make the elevators go up or down)
S1;S2 - Motors on the shoulders (to flip the shoulder up or down)
SV1 - Servo which holds the Camera (to make the camera rotate)
gyro - To detect the direction of the robot (by using angles)
auto - A variable for setting different choices of autonomous session
autoState - Different steps in each route in AutonomousPeriodic
SW0 - The switch at the spot where the elevator should be stopped (lower)
SW1 - The switch at the spot where the elevator should be stopped (higher)

Timeline:
The days before Mar.7 - We started designing the GUI(We determined what data we should display);
                        We finished coding the Gyro;
                        We finished coding the motor;
                        We finished coding the Pneumatic system;
                        We assigned all the variables needed;
                        We finished coding the switches... etc.
                        
Mar.7 - We coded the Encoder as well as the state machines and tested the code with our test robot. They worked;
        We made a list of all the variables.

The days between Mar.8 and Mar.12 - We finished coding all the options in the AutonomousPeriodic;
                                    We started coding reset function(only for the test robot);

Mar.12 - We checked the codes and tested the buttons for periodic - they worked;
         We started coding for vision processing.
        
Mar.13 - We Started making a brand new GUI (formal version for competitions);
         We kept calculating data for the code in Autonomousperodic;
         We stopped coding the reset function because we found out that we actually did not need it for our real robot;
         We modified codes to allow our robot to rotate without moving forward.
         
Mar.14 - We Kept calculating data for the code in Autonomousperodic. 
(the distance the robot needed to travel to get to the scale/switch, the angle the robot needed to rotate for, etc.)

Mar.15 - We finished the autonomous code and completed the robotcode;
         The comments are also completed;
         Networktable part is ready for gui.
         
Mar.16 - We debugged the robot code with the help of Leo;
         We adapted the autonomous code as a compromise;
         We decided to use Java instead of Python for robot code in upcoming games;
         We had a meeting and got a basic idea of robot.Java.
         We developed a basic version of our robot code in Java.
         
Mar.17 - We used the Java code in competitions.

Mar.18 - We learned some basic ideas about Java as preparation.

Mar.19 - We Had Eclipse and Notepad++ installed on our computers;
         We Started the new robot.Java project;
         
Mar.20 - We got a basic plan for robot.java;
         We decided to use command-based programming for our robot code.(commands and subsystems)
         We learned to use Eclipse and Java by trial and error;
         We Understood all the lines in the sample robot.java.

Mar.21 - We developed a detailed plan about our command-based programming.
         We kept learning the basics of Java and the command-based programming.
    
         
         
         


"""

