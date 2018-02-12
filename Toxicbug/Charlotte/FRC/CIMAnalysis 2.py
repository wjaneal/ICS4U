#FRC 6162
#Power Up
#CIM motor analysis - crate intake
from math import *
pi = 4*atan(1.0)
g = 9.8
robotLength = 0.83
robotHeight = 1.39
baseHeight = 0.15
wheelRadius = 0.095
rampAngle = 180/pi*atan(robotHeight-baseHeight)/robotLength
print(rampAngle)
heightRecord = [0,0]
for i in range(1,1000):
    ratio = i
    motorRPM = 4000
    motorTorque = 0.43
    wheelRPM =  motorRPM/ratio
    cubeMass = 1.6
    wheelTorque = motorTorque*ratio
    wheelForce = wheelTorque/wheelRadius
    accelerationDistance = 0.4
    Fg = cubeMass*g*sin(rampAngle*pi/180)
    Fw = wheelForce
    F = (Fw-Fg)*(1-0.2)
    if F < 0:
        F = 0
    a = F/cubeMass
    vExit = sqrt(2*a*accelerationDistance)
    #if a >  0:
    #    t1=vExit/a
    vExitY = vExit*sin(rampAngle*pi/180)
    d
    
    = vExitY**2/(2*9.8)
    wheelRPS = wheelRPM/60
    wheelSpeed = wheelRPS*2*pi*wheelRadius
    vExit2= wheelSpeed
    vExit2Y=vExit2*sin(rampAngle*pi/180)
    d2 = vExit2Y**2/(2*9.8)
    if (d>0.44 and d2 > 0.44):
        print("From Torque:",d,"From RPM:",d2,ratio)



