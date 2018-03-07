# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 12:53:59 2018

@author: fy

ICS4U ISP - FRC Project

Planning Technique - Agile - Planning and test together quickly throughout all the sessions involved.

Group members:Charlotte, Emma and Khan

Content:
①Framework - construction of robot.py; Organization of names of variables
②GUI - interface of displaying the data we wre using
③Encoder - detection of distance and time
④Motor - movement of robot
⑤Gyro - direction of robot
⑥State Machine - a series of movement
⑦Pneumatic Systems - a controller of the arms
⑧Switches - spots of stopping

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









"""

