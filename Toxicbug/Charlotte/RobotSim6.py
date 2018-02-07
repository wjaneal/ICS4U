#<<<<<<< HEAD
#FRC Robot Climbing Simulator
#Written by Charlotte Chen and William Neal
#Email contact: charlottechen418@gmail.com, wneal@lia-edu.ca
#Team 6162 Cap Alpaca
#London International Academy
#London, ON
#=======
#This is a GUI program using classes for organization
#>>>>>>> master


#Read - import required modules
import tkinter
import sys
from math import *
import math
from tkinter import font
from tkinter import messagebox
from tkinter import *
import time

        
        
#<<<<<<< HEAD
#This function is not currently being used - November 6, 2017
#=======

#>>>>>>> master
def motorPower(RPM):
    #Approximate data for Vex 775Pro taken from datasheet
    return -0.00000425983*(RPM-9370.0)**2+347.0

#<<<<<<< HEAD

#This function initialized a "Robot" object with all of the data required for climbing calculations.
class RobotC(object):
    def __init__(self,G1,G2,G3,G4,Gear1,Gear2,Gear3,Gear4,S1,S2,ratio,Drive_Torque,Max_Force,Climber_RPM,Climber_Frequency,Climb_Speed,Climb_Time,Required_Power,Mass):
        RC=[]
        self.G1=G1#0, 2 or 4 gears allowed in our climbing competition.
        self.G2=G2
        self.G3=G3
        self.G4=G4
        self.Gear1=Gear1
        self.Gear2=Gear2
        self.Gear3=Gear3
        self.Gear4=Gear4
        self.S1=S1 #0, 1 or 2 planetary gear stages are allowed
        self.S2=S2
        self.ratio=ratio #Variable to store the gear ratio arising from all of the gear stages.
        self.Drive_Torque=Drive_Torque #Other variables; names indicate use.
#=======
class RobotC(object):
    def __init__(self,G1,G2,G3,G4,Geal1,Geal2,Geal3,Geal4,S1,S2,ratio,Drive_Torque,Max_Force,Climber_RPM,Climber_Frequency,Climb_Speed,Climb_Time,Required_Power,Mass):
        RC=[]
        self.G1=G1
        self.G2=G2
        self.G3=G3
        self.G4=G4
        self.Geal1=Geal1
        self.Geal2=Geal2
        self.Geal3=Geal3
        self.Geal4=Geal4
        self.S1=S1
        self.S2=S2
        self.ratio=ratio
        self.Drive_Torque=Drive_Torque
#>>>>>>> master
        self.Max_Force=Max_Force
        self.Climber_RPM=Climber_RPM
        self.Climber_Frequency=Climber_Frequency
        self.Climb_Speed=Climb_Speed
        self.Climb_Time=Climb_Time
        self.Required_Power=Required_Power
        self.Mass=Mass
              
            


#MenuBar class - called by the main class
class MenuBar(tkinter.Menu):
    def __init__(self, parent, bg="lightgreen"):
        helv14b = font.Font(family="DejaVu Sans",size=14,weight="bold")
        helv14B = helv14b
        helv18B = font.Font(family="DejaVu Sans",size=18,weight="bold")
        tkinter.Menu.__init__(self, parent)
        self.Mass = tkinter.StringVar()
        self.Distance = tkinter.StringVar()
        self.AR = tkinter.StringVar()
        self.G1 = tkinter.StringVar()
        self.G2 = tkinter.StringVar()
        self.G3 = tkinter.StringVar()
        self.G4 = tkinter.StringVar()
        self.S1 = tkinter.StringVar()
        self.S2 = tkinter.StringVar()
        self.Drive_Torque_str = tkinter.StringVar()
        self.Gravitational_Force_str = tkinter.StringVar()
        self.Max_Force_str = tkinter.StringVar()
        self.Robot_Force_str = tkinter.StringVar()
        self.Net_Force_str = tkinter.StringVar()
        self.possible_str = tkinter.StringVar()
        self.Motor_RPM_str = tkinter.StringVar()
        self.Ratio_str = tkinter.StringVar()
        self.Climber_RPM_str = tkinter.StringVar()
        self.Climber_Frequency_str = tkinter.StringVar()
        self.Climb_Speed_str = tkinter.StringVar()
        self.Climb_Time_str = tkinter.StringVar()
        self.Required_Power_str = tkinter.StringVar()
        self.Motor_Power_str = tkinter.StringVar()
        self.Motor_Torque_str = tkinter.StringVar()
        self.GForce = tkinter.StringVar()
        self.GForce1 = tkinter.StringVar()
        self.T = tkinter.StringVar()
        self.ratio1 = tkinter.StringVar()
        self.var = IntVar()
        #self.friction_str = tkinter.StringVar()
        
        
        #Basic Quantities
        self.g = 9.8 #Gravitational Constant
        self.pi = 4*math.atan(1.0) #Pi
        self.amperes = 37 #Current to run through the motor - set at an amount 
        #self.friction = 0.1 #Friction loss at each gear stage
        #close to but not too close to the limit of 40 amperes imposed by the circuit breaker
        
        #Graphical Display Data:
        self.X_INIT = 200
        self.ROBOT_SPACE = 50
        self.ROBOT_HEIGHT = 25
        self.ROBOT_WIDTH = 25
        self.X_MIN = 0
        self.X_MAX = 600
        self.Y_MIN = 0
        self.Y_MAX = 700
        self.FLOOR_HEIGHT = 100
        self.CEILING_HEIGHT = 100
        self.CLIMB_HEIGHT = self.Y_MAX-self.Y_MIN-self.CEILING_HEIGHT-self.FLOOR_HEIGHT-self.ROBOT_HEIGHT
        self.Y_INIT = self.Y_MAX-self.FLOOR_HEIGHT-self.ROBOT_HEIGHT
        self.TIME_DELAY = 0.00025
        self.Climb_Time = 1.0
        self.RC=[]
        for i in range(0,3):
            self.RC.append(RobotC(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
        
        
        simMenu = tkinter.Menu(self, tearoff=False, font=helv14b)
        simMenu.add_command(label="Simulate", command=self.sim, accelerator="Ctrl+S", underline=0)
        simMenu.add_command(label="Gravitational Force", command=self.gravitationalForce)
        simMenu.add_command(label="Torque", command=self.torque)
        simMenu.add_command(label="Gear Ratios", command=self.gearRatios)       
        simMenu.add_command(label="Settings", command=self.settings, accelerator="Ctrl+E", underline=1)
        self.add_cascade(label="Simulation", menu=simMenu)
        exitMenu = tkinter.Menu(self, tearoff=False, font=helv14b)
        exitMenu.add_command(label="Exit", command=self.quit)
        self.add_cascade(label="Exit", menu=exitMenu)
        self.canvas = tkinter.Canvas(parent,width=500,height=800,bg="white")
        self.canvas.grid(row=0,rowspan=14,column=0)
        #self.filename=tkinter.PhotoImage(master=self.canvas, file="MathBackground.gif")
        #self.image1=self.canvas.create_image(10,10,image=self.filename)
        #self.canvas.pack()
        
        #Column 1 - Labels
        self.title_label = tkinter.Label(parent, text="Robot Data", font = helv18B, bg="lightgreen", justify=LEFT).grid(sticky="W", row=0, column=1, columnspan=2)
        self.mass_label = tkinter.Label(parent, text="Robot Mass:", font = helv14B, bg="lightgreen",borderwidth=1, justify=LEFT, relief=SUNKEN).grid(sticky="W",row=1, column=1)
        self.distance_label = tkinter.Label(parent, text="Distance to Climb:", font = helv14B, bg="lightgreen", justify=LEFT, relief=SUNKEN ).grid(sticky="W", row=2, column=1)
        self.radius_label = tkinter.Label(parent, text="Climber Axle Radius:", font = helv14B, bg="lightgreen", justify=LEFT, borderwidth=2, relief=SUNKEN).grid(sticky="W",row=3, column=1)
        self.G1_label = tkinter.Label(parent, text="Gear 1:", font = helv14B, bg="lightgreen", justify=LEFT, borderwidth=2, relief=SUNKEN).grid(sticky="W", row=4, column=1)
        self.G2_label = tkinter.Label(parent, text="Gear 2:", font = helv14B, bg="lightgreen", justify=LEFT, borderwidth=2, relief=SUNKEN).grid(sticky="W", row=5, column=1)
        self.G3_label = tkinter.Label(parent, text="Gear 3:", font = helv14B, bg="lightgreen", justify=LEFT, borderwidth=2, relief=SUNKEN).grid(sticky="W", row=6, column=1)
        self.G4_label = tkinter.Label(parent, text="Gear 4:", font = helv14B, bg="lightgreen", justify=LEFT, borderwidth=2, relief=SUNKEN).grid(sticky="W", row=7, column=1)
        self.S1_label = tkinter.Label(parent, text="Planetary Stage 1:", font = helv14B, bg="lightgreen", justify=LEFT, borderwidth=2, relief=SUNKEN).grid(sticky="W", row=8, column=1)
        self.S2_label = tkinter.Label(parent, text="Planetary Stage 2:", font = helv14B, bg="lightgreen", justify=LEFT, borderwidth=2, relief=SUNKEN).grid(sticky="W", row=9, column=1)
        
        #Column 2 - Amounts / Quantities
        self.mass_data = tkinter.Label(parent, textvariable=self.Mass, font = helv14B, bg="lightgreen").grid(sticky="E", row=1,column=2)
        self.distance_note = tkinter.Label(parent, textvariable=self.Distance, font = helv14B, bg="lightgreen").grid(sticky="E", row=2,column=2)
        self.radius_note = tkinter.Label(parent, textvariable=self.AR, font = helv14B, bg="lightgreen").grid(sticky="E", row=3,column=2)
        self.G1_note = tkinter.Label(parent, textvariable=self.G1, font = helv14B, bg="lightgreen").grid(sticky="E", row=4,column=2)
        self.G2_note = tkinter.Label(parent, textvariable=self.G2, font = helv14B, bg="lightgreen").grid(sticky="E", row=5,column=2)
        self.G3_note = tkinter.Label(parent, textvariable=self.G3, font = helv14B, bg="lightgreen").grid(sticky="E", row=6,column=2)
        self.G4_note = tkinter.Label(parent, textvariable=self.G4, font = helv14B, bg="lightgreen").grid(sticky="E", row=7,column=2)
        self.S1_note = tkinter.Label(parent, textvariable=self.S1, font = helv14B, bg="lightgreen").grid(sticky="E", row=8,column=2)
        self.S2_note = tkinter.Label(parent, textvariable=self.S2, font = helv14B, bg="lightgreen").grid(sticky="E", row=9,column=2)
        
        #Column 3 - Units
        self.mass_unit = tkinter.Label(parent, text="kg", font = helv14B, bg="lightgreen").grid(sticky="W",row=1, column=3)
        self.distance_unit = tkinter.Label(parent, text="m", font = helv14B, bg="lightgreen").grid(sticky="W",row=2, column=3)
        self.radius_unit = tkinter.Label(parent, text="m", font = helv14B, bg="lightgreen").grid(sticky="W",row=3, column=3)
        self.G1_unit = tkinter.Label(parent, text="teeth", font = helv14B, bg="lightgreen").grid(sticky="W",row=4, column=3)
        self.G2_unit = tkinter.Label(parent, text="teeth", font = helv14B, bg="lightgreen").grid(sticky="W",row=5, column=3)
        self.G3_unit = tkinter.Label(parent, text="teeth", font = helv14B, bg="lightgreen").grid(sticky="W",row=6, column=3)
        self.G4_unit = tkinter.Label(parent, text="teeth", font = helv14B, bg="lightgreen").grid(sticky="W",row=7, column=3)
        self.S1_unit = tkinter.Label(parent, text="teeth", font = helv14B, bg="lightgreen").grid(sticky="W",row=8, column=3)
        self.S2_unit = tkinter.Label(parent, text="teeth", font = helv14B, bg="lightgreen").grid(sticky="W",row=9, column=3)
        
        #Column 4: Data Labels
        
        self.Drive_Torque_label = tkinter.Label(parent, text = "Drive Torque: ", font = helv14B, bg = "lightgreen", borderwidth=2, relief=SUNKEN).grid(sticky="W", row = 1, column=4)        
        self.Max_Force_label = tkinter.Label(parent, text = "Maximum Force: ", font = helv14B, bg = "lightgreen", borderwidth=2, relief=SUNKEN).grid(sticky="W", row = 2, column=4)        
        self.Gravitational_Force_label = tkinter.Label(parent, text = "Gravitational Force: ", font = helv14B, bg = "lightgreen", borderwidth=2, relief=SUNKEN).grid(sticky="W", row = 3, column=4)        
        self.Net_Force_label = tkinter.Label(parent, text = "Net Force: ", font = helv14B, bg = "lightgreen", borderwidth=2, relief=SUNKEN).grid(sticky="W", row = 4, column=4)        
        self.possible_label = tkinter.Label(parent, text = "Possible?", font = helv14B, bg = "lightgreen", borderwidth=2, relief=SUNKEN).grid(sticky="W", row = 5, column=4)        
        self.Motor_RPM_label = tkinter.Label(parent, text = "Motor RPM: ", font = helv14B, bg = "lightgreen", borderwidth=2, relief=SUNKEN).grid(sticky="W", row = 6, column=4)        
        self.Ratio_label = tkinter.Label(parent, text = "Gear Ratio: ", font = helv14B, bg = "lightgreen", borderwidth=2, relief=SUNKEN).grid(sticky="W", row = 7, column=4)                
        self.Climber_RPM_label = tkinter.Label(parent, text = "Climber_RPM", font = helv14B, bg = "lightgreen", borderwidth=2, relief=SUNKEN).grid(sticky="W", row = 8, column=4)        
        self.Climber_Frequency_label = tkinter.Label(parent, text = "Climber Frequency: ", font = helv14B, bg = "lightgreen", borderwidth=2, relief=SUNKEN).grid(sticky="W", row = 9, column=4)        
        self.Climb_Speed_label = tkinter.Label(parent, text = "Climb Speed:", font = helv14B, bg = "lightgreen", borderwidth=2, relief=SUNKEN).grid(sticky="W", row = 10, column=4)        
        self.Climb_Time_label = tkinter.Label(parent, text = "Climb Time:", font = helv14B, bg = "lightgreen", borderwidth=2, relief=SUNKEN).grid(sticky="W", row = 11, column=4)        
        self.Motor_Power_label = tkinter.Label(parent, text = "Motor Power: ", font = helv14B, bg = "lightgreen", borderwidth=2, relief=SUNKEN).grid(sticky="W", row = 12, column=4)        
        
        #Column 5: Data Amounts and Quantities
        self.Drive_Torque_variable = tkinter.Label(parent, textvariable=self.Drive_Torque_str, font = helv14B, bg="lightgreen").grid(sticky="E", row=1,column=5)
        self.Max_Force_variable = tkinter.Label(parent, textvariable=self.Max_Force_str, font = helv14B, bg="lightgreen").grid(sticky="E", row=2,column=5)
        self.Gravitational_Force_variable = tkinter.Label(parent, textvariable=self.Gravitational_Force_str, font = helv14B, bg="lightgreen").grid(sticky="E", row=3,column=5)
        self.Net_Force_variable = tkinter.Label(parent, textvariable=self.Net_Force_str, font = helv14B, bg="lightgreen").grid(sticky="E", row=4,column=5)
        self.possible_variable = tkinter.Label(parent, textvariable=self.possible_str, font = helv14B, bg="lightgreen").grid(sticky="E", row=5,column=5)
        self.Motor_RPM_variable = tkinter.Label(parent, textvariable=self.Motor_RPM_str, font = helv14B, bg="lightgreen").grid(sticky="E", row=6,column=5)
        self.Ratio_variable = tkinter.Label(parent, textvariable=self.Ratio_str, font=helv14B, bg="lightgreen").grid(sticky="E", row=7,column=5)
        self.Climber_RPM_variable = tkinter.Label(parent, textvariable=self.Climber_RPM_str, font = helv14B, bg="lightgreen").grid(sticky="E", row=8,column=5)
        self.Climber_Frequency_variable = tkinter.Label(parent, textvariable=self.Climber_Frequency_str, font = helv14B, bg="lightgreen").grid(sticky="E", row=9,column=5)
        self.Climb_Speed_variable = tkinter.Label(parent, textvariable=self.Climb_Speed_str, font = helv14B, bg="lightgreen").grid(sticky="E", row=10,column=5)
        self.Climb_Time_variable = tkinter.Label(parent, textvariable=self.Climb_Time_str, font = helv14B, bg="lightgreen").grid(sticky="E", row=11,column=5)
        self.Motor_Power_variable = tkinter.Label(parent, textvariable=self.Motor_Power_str, font = helv14B, bg="lightgreen").grid(sticky="E", row=12,column=5)
    
        
        #Column 6: Data Units
        self.Drive_Torque_unit = tkinter.Label(parent, text = "Nm", font = helv14B, bg = "lightgreen", borderwidth=2).grid(sticky="W", row = 1, column=6)        
        self.Max_Force_unit = tkinter.Label(parent, text = "N", font = helv14B, bg = "lightgreen", borderwidth=2).grid(sticky="W", row = 2, column=6)        
        self.Gravitational_unit_label = tkinter.Label(parent, text = "N", font = helv14B, bg = "lightgreen", borderwidth=2).grid(sticky="W", row = 3, column=6)        
        self.Net_Force_unit = tkinter.Label(parent, text = "N", font = helv14B, bg = "lightgreen", borderwidth=2).grid(sticky="W", row = 4, column=6)               
        self.Motor_RPM_unit = tkinter.Label(parent, text = "RPM", font = helv14B, bg = "lightgreen", borderwidth=2).grid(sticky="W", row = 6, column=6)        
        self.Ratio_unit = tkinter.Label(parent, text = "(no unit)", font = helv14B, bg = "lightgreen", borderwidth=2).grid(sticky="W", row = 7, column=6)                
        self.Climber_RPM_unit = tkinter.Label(parent, text = "RPM", font = helv14B, bg = "lightgreen", borderwidth=2).grid(sticky="W", row = 8, column=6)        
        self.Climber_Frequency_unit = tkinter.Label(parent, text = "/s", font = helv14B, bg = "lightgreen", borderwidth=2).grid(sticky="W", row = 9, column=6)        
        self.Climb_Speed_unit = tkinter.Label(parent, text = "m/s", font = helv14B, bg = "lightgreen", borderwidth=2).grid(sticky="W", row = 10, column=6)        
        self.Climb_Time_unit = tkinter.Label(parent, text = "s", font = helv14B, bg = "lightgreen", borderwidth=2).grid(sticky="W", row = 11, column=6)        
        self.Motor_Power_unit = tkinter.Label(parent, text = "W", font = helv14B, bg = "lightgreen", borderwidth=2).grid(sticky="W", row = 12, column=6)        
       
        
        
    def settings(self): #This function applies the settings for robot data to each other function in the program
        helv14B = font.Font(family="DejaVu Sans Sans",size=14,weight="bold")
        helv18B = font.Font(family="DejaVu Sans",size=18,weight="bold")
        self.filewin = tkinter.Toplevel(self, bg="lightgreen")
        #Create default variable values:
        self.Mass.set(20)
        self.Distance.set(2.0)
        self.AR.set(0.015)
        self.G1.set(72)
        self.G2.set(30)
        self.G3.set(54)
        self.G4.set(18)
        self.S1.set(10)
        self.S2.set(1)
        #Display the widgets:
        self.mass_label = tkinter.Label(self.filewin, text="Robot Mass:", font = helv14B, bg="lightgreen").grid(row=1, column=0)
        self.mass_entry = tkinter.Entry(self.filewin, textvariable=self.Mass, font = helv14B)
        self.mass_entry.grid(row=1,column=1)
        self.mass_note = tkinter.Label(self.filewin, text="kg", font = helv14B, bg="lightgreen").grid(row=1,column=2)
        self.distance_label = tkinter.Label(self.filewin, text="Distance to Climb:", font = helv14B, bg="lightgreen").grid(row=2, column=0)
        self.distance_entry= tkinter.Entry(self.filewin, textvariable=self.Distance, font = helv14B)
        self.distance_entry.grid(row=2,column=1)
        self.distance_note = tkinter.Label(self.filewin, text="m", font = helv14B, bg="lightgreen").grid(row=2,column=2)
        self.radius_label = tkinter.Label(self.filewin, text="Climber Axle Radius:", font = helv14B, bg="lightgreen").grid(row=3, column=0)
        self.radius_entry = tkinter.Entry(self.filewin, textvariable=self.AR, font = helv14B)
        self.radius_entry.grid(row=3,column=1)
        self.radius_note = tkinter.Label(self.filewin, text="m", font = helv14B, bg="lightgreen").grid(row=3,column=2)
        self.G1_label = tkinter.Label(self.filewin, text="Gear 1 (leave blank if none):", font = helv14B, bg="lightgreen").grid(row=4, column=0)
        self.G1_entry = tkinter.Entry(self.filewin, textvariable=self.G1, font = helv14B)
        self.G1_entry.grid(row=4,column=1)
        self.G1_note = tkinter.Label(self.filewin, text="teeth", font = helv14B, bg="lightgreen").grid(row=4,column=2)
        self.G2_label = tkinter.Label(self.filewin, text="Gear 2 (leave blank if none):", font = helv14B, bg="lightgreen").grid(row=5, column=0)
        self.G2_entry = tkinter.Entry(self.filewin, textvariable=self.G2, font = helv14B)
        self.G2_entry.grid(row=5,column=1)
        self.G2_note = tkinter.Label(self.filewin, text="teeth", font = helv14B, bg="lightgreen").grid(row=5,column=2)
        self.G3_label = tkinter.Label(self.filewin, text="Gear 3 (leave blank if none):", font = helv14B, bg="lightgreen").grid(row=6, column=0)
        self.G3_entry = tkinter.Entry(self.filewin, textvariable=self.G3, font = helv14B)
        self.G3_entry.grid(row=6,column=1)
        self.G3_note = tkinter.Label(self.filewin, text="teeth", font = helv14B, bg="lightgreen").grid(row=6,column=2)
        self.G4_label = tkinter.Label(self.filewin, text="Gear 4 (leave blank if none):", font = helv14B, bg="lightgreen").grid(row=7, column=0)
        self.G4_entry = tkinter.Entry(self.filewin, textvariable=self.G4, font = helv14B)
        self.G4_entry.grid(row=7,column=1)
        self.G4_note = tkinter.Label(self.filewin, text="teeth", font = helv14B, bg="lightgreen").grid(row=7,column=2)
        self.S1_label = tkinter.Label(self.filewin, text="Planetary Stage 1 (leave blank if none):", font = helv14B, bg="lightgreen").grid(row=8, column=0)
        self.S1_entry = tkinter.Entry(self.filewin, textvariable=self.S1, font = helv14B)
        self.S1_entry.grid(row=8,column=1)
        self.S1_note = tkinter.Label(self.filewin, text="teeth", font = helv14B, bg="lightgreen").grid(row=8,column=2)
        self.S2_label = tkinter.Label(self.filewin, text="Planetary Stage 2 (leave blank if none):", font = helv14B, bg="lightgreen").grid(row=9, column=0)
        self.S2_entry = tkinter.Entry(self.filewin, textvariable=self.S2, font = helv14B)
        self.S2_entry.grid(row=9,column=1)
        self.S2_note = tkinter.Label(self.filewin, text="teeth", font = helv14B, bg="lightgreen").grid(row=9,column=2) 
        self.Radiobutton1 = tkinter.Radiobutton(self.filewin, text="Team 1", variable=self.var, value=0,bg="lightgreen")
        self.Radiobutton1.grid(row=10,column=0)
        self.Radiobutton2 = tkinter.Radiobutton(self.filewin, text="Team 2", variable=self.var, value=1,bg="lightgreen")
        self.Radiobutton2.grid(row=10,column=1)
        self.Radiobutton3 = tkinter.Radiobutton(self.filewin, text="Team 3", variable=self.var, value=2,bg="lightgreen")
        self.Radiobutton3.grid(row=10,column=2)
        self.enter_settings = tkinter.Button(self.filewin, text = "Enter Settings", font = helv14B, bg="green",command=self.climbingCalculations).grid(row=11,column=1)
        
    def climbingCalculations(self): #This function completes calculations used in the robot climbing simultation
        #Read the gear data from the form and create the self.gears list
        self.currentRC = self.var.get()
        self.RC[self.currentRC].G1 = self.G1.get()
        self.RC[self.currentRC].G2 = self.G2.get()
        self.RC[self.currentRC].G3 = self.G3.get()
        self.RC[self.currentRC].G4 = self.G4.get()
        self.RC[self.currentRC].S1 = self.S1.get()
        self.RC[self.currentRC].S2 = self.S2.get()
        self.RC[self.currentRC].ratio = 1
        if self.RC[self.currentRC].G1 == "":
            self.RC[self.currentRC].Gear1 = 0
        else:
            self.RC[self.currentRC].Gear1 = float(self.RC[self.currentRC].G1)
        if self.RC[self.currentRC].G2 == "":
            self.RC[self.currentRC].Gear2 = 0
        else:
            self.RC[self.currentRC].Gear2 = float(self.RC[self.currentRC].G2)
        if self.RC[self.currentRC].G3 == "":
            self.RC[self.currentRC].Gear3 = 0
        else:
            self.RC[self.currentRC].Gear3 = float(self.RC[self.currentRC].G3)
        if self.RC[self.currentRC].G4 == "":
            self.RC[self.currentRC].Gear4 = 0
        else:
            self.RC[self.currentRC].Gear4 = float(self.RC[self.currentRC].G4)
        self.gears=[]
        if self.RC[self.currentRC].Gear1 == 0 or self.RC[self.currentRC].Gear2 ==0:
            pass
        else:
            self.gears.append(self.RC[self.currentRC].Gear1)
            self.gears.append(self.RC[self.currentRC].Gear2)
        if self.RC[self.currentRC].Gear3 == 0 or self.RC[self.currentRC].Gear4 ==0:
            pass
        else:
            self.gears.append(self.RC[self.currentRC].Gear3)
            self.gears.append(self.RC[self.currentRC].Gear4)
        #Calculate the gear ratio based on the gears stage:
                #Zero, Two or four gears may be used here.
        if len(self.gears)==4:
            self.RC[self.currentRC].ratio = 1.0/(self.gears[0]/self.gears[1]*self.gears[2]/self.gears[3])
        elif len(self.gears)==2:
            self.RC[self.currentRC].ratio = 1.0/(self.gears[0]/self.gears[1])
        else:  #Only 0, 2 or 4 gears are acceptable.  Assume no gears if not 2 or 4
            self.RC[self.currentRC].ratio = 1.0
        #Further ratio calculations from the planetary gear stage:
        self.RC[self.currentRC].S1=self.S1.get()
        self.RC[self.currentRC].S2=self.S2.get()
        self.stages=[] 
        if self.RC[self.currentRC].S1=="" or self.RC[self.currentRC].S1=="0":
            pass
        else:
            self.stages.append(int(self.RC[self.currentRC].S1))
            
        if self.RC[self.currentRC].S2=="" or self.RC[self.currentRC].S2=="0":
            pass
        else:
            self.stages.append(int(self.RC[self.currentRC].S2))
        for i in self.stages:
            self.RC[self.currentRC].ratio*=i
        #0 1 or 2 are allowed.  
        self.RC[self.currentRC].Climb_Distance = float(self.Distance.get()) #Distance the robot needs to climb
        self.RC[self.currentRC].Axle_Radius = float(self.AR.get())
        self.RC[self.currentRC].Mass=float(self.Mass.get()) 
        
        #Motor Data
        self.Stall_Current = 134.0
        self.Stall_Torque=0.71
        self.Efficiency = (100.0-5.0*len(self.gears)-5.0*len(self.stages))/100.0 #Estimate 5% loss per gear or stage
        self.Free_Speed = 18730

        #Calculations
        self.Motor_Torque = self.amperes*self.Stall_Torque/self.Stall_Current*self.Efficiency
        self.Motor_RPM = self.Free_Speed*(self.Motor_Torque-self.Stall_Torque)/(-self.Stall_Torque)
        self.RC[self.currentRC].Drive_Torque = 1.0*self.Motor_Torque*self.RC[self.currentRC].ratio
        #print ("Ratio: ", self.ratio)
        self.RC[self.currentRC].Max_Force = self.RC[self.currentRC].Drive_Torque/self.RC[self.currentRC].Axle_Radius
        self.Gravitational_Force = self.RC[self.currentRC].Mass*self.g
        #self.Robot_Force = self.mass*self.g*self.Axle_Radius
        self.RC[self.currentRC].Net_Force = self.RC[self.currentRC].Max_Force-self.Gravitational_Force
        if self.RC[self.currentRC].Net_Force <= 0:
            self.possible = False
            #self.possible_variable.bg="red"
        else:
            self.possible = True
            #self.possible_variable.bg="green"
        self.RC[self.currentRC].Climber_RPM =self.Motor_RPM/self.RC[self.currentRC].ratio
        self.RC[self.currentRC].Climber_Frequency = self.RC[self.currentRC].Climber_RPM/60.0
        self.RC[self.currentRC].Climb_Speed = self.RC[self.currentRC].Climber_Frequency * 2 * self.pi * self.RC[self.currentRC].Axle_Radius
        self.RC[self.currentRC].Climb_Time = self.RC[self.currentRC].Climb_Distance/self.RC[self.currentRC].Climb_Speed
        #print(self.Climb_Distance)
        #print(self.Climb_Speed)
        #print(self.Climb_Time)
        self.RC[self.currentRC].Required_Power = self.RC[self.currentRC].Mass*self.g*self.RC[self.currentRC].Climb_Distance/self.RC[self.currentRC].Climb_Time
        self.Motor_Power = motorPower(self.Motor_RPM)
        
        #Update displayed values:
        
        self.Motor_Torque_str.set("%.2f" % self.Motor_Torque)
        self.Max_Force_str.set("%.2f" % self.RC[self.currentRC].Max_Force)
        self.Motor_RPM_str.set("%.2f" % self.Motor_RPM)
        self.Ratio_str.set("%.2f" % self.RC[self.currentRC].ratio)
        self.Drive_Torque_str.set("%.2f" % self.RC[self.currentRC].Drive_Torque)
        self.Gravitational_Force_str.set("%.2f" % self.Gravitational_Force)
        self.Max_Force_str.set("%.2f" % self.RC[self.currentRC].Max_Force)
        self.Net_Force_str.set("%.2f" % self.RC[self.currentRC].Net_Force)
        
        if self.possible==True:
            self.possible_str.set("True")
            self.Climber_RPM_str.set("%.2f" % self.RC[self.currentRC].Climber_RPM)
            self.Climber_Frequency_str.set("%.2f" % self.RC[self.currentRC].Climber_Frequency)
            self.Climb_Speed_str.set("%.2f" % self.RC[self.currentRC].Climb_Speed)
            self.Climb_Time_str.set("%.2f" % self.RC[self.currentRC].Climb_Time)
            self.Required_Power_str.set("%.2f" % self.RC[self.currentRC].Required_Power)
            self.Motor_Power_str.set("%.2f" % self.Motor_Power)
        else:
            self.possible_str.set("False")
            self.Climber_RPM_str.set("N/A")
            self.Climber_Frequency_str.set("N/A")
            self.Climb_Speed_str.set("N/A")
            self.Climb_Time_str.set("N/A")
            self.Required_Power_str.set("N/A")
            self.Motor_Power_str.set("N/A")
        #print(self.RC[1].ratio)
        #print(self.RC[self.currentRC].Net_Force)
        self.filewin.destroy()
    
    def gravitationalForce(self): #Calculates the gravitational force generated by a mass on a rope.
        print ("Calculate gravitational force")
        helv14B = font.Font(family="DejaVu Sans Sans",size=14,weight="bold")
        helv18B = font.Font(family="DejaVu Sans",size=18,weight="bold")
        self.filewin = tkinter.Toplevel(self, bg="lightgreen")
        self.title_label = tkinter.Label(self.filewin,text="Calculate the gravitational Force",font=helv18B,bg="lightgreen").grid(row=0,column=0,columnspan=2)
        self.mass_label = tkinter.Label(self.filewin,text="Robot Mass:",font = helv14B,bg="lightgreen").grid(row=1,column=0)
        self.mass_entry = tkinter.Entry(self.filewin,font=helv14B,textvariable=self.Mass,bg="lightgreen")
        self.mass_entry.grid(row=1,column=1)
        self.mass_note = tkinter.Label(self.filewin, text="kg", font = helv14B, bg="lightgreen").grid(row=1,column=2)
        self.Calculate_button = tkinter.Button(self.filewin,text="Calculate",font = helv14B,bg="lightgreen",command=self.CalculateGForce).grid(row=2,column=1)
        self.GForce_label = tkinter.Label(self.filewin,text="Gravitational Force:",font = helv14B,bg="lightgreen").grid(row=3,column=0)
        self.GForce_variable = tkinter.Label(self.filewin,textvariable=self.GForce,font = helv14B,bg="lightgreen").grid(row=3,column=1)
        self.GForce_unit = tkinter.Label(self.filewin,text="N",font = helv14B, bg="lightgreen").grid(row=3,column=2)
        
    def CalculateGForce(self):
        self.mass = float(self.Mass.get())
        self.Gforce = self.mass*self.g
        self.GForce.set("%.2f" % self.Gforce)
       
    def torque(self): #Calculates torque applied on an axle from a mass tied to a rope around the axle
        print ("Calculate torque applied on an axle from a mass tied to a rope around the axle")
        self.filewin = tkinter.Toplevel(self,bg="lightgreen")
        helv14B = font.Font(family="DejaVu Sans Sans",size=14,weight="bold")
        helv18B = font.Font(family="DejaVu Sans",size=18,weight="bold")
        self.title_label = tkinter.Label(self.filewin,text="Calculate torque",font=helv18B,bg="lightgreen").grid(row=0,column=0,columnspan=2)
        self.mass_label = tkinter.Label(self.filewin,text="Robot Mass:",font = helv14B,bg="lightgreen").grid(row=1,column=0)
        self.mass_entry = tkinter.Entry(self.filewin,font=helv14B,textvariable=self.Mass)
        self.mass_entry.grid(row=1,column=1)
        self.mass_note = tkinter.Label(self.filewin, text="kg", font = helv14B, bg="lightgreen").grid(row=1,column=2)
        #self.GForce_label = tkinter.Label(self.filewin,text="Gravitational Force:", font = helv14B,bg="lightgreen").grid(row=2,column=0)
        #self.GForce_variable = tkinter.Label(self.filewin,textvariable=self.GForce1,font=helv14B,bg="lightgreen")
        #self.GForce_variable.grid(row=2,column=1)
        self.radius_label = tkinter.Label(self.filewin, text="Climber Axle Radius:", font = helv14B, bg="lightgreen").grid(row=2, column=0)
        self.radius_variable = tkinter.Entry(self.filewin, textvariable=self.AR, font = helv14B)
        self.radius_variable.grid(row=2,column=1)
        self.radius_note = tkinter.Label(self.filewin, text="m", font = helv14B, bg="lightgreen").grid(row=2,column=2)
        self.calculate_label = tkinter.Button(self.filewin,text="Calculate",command=self.calculateT).grid(row=3,column=1)
        self.torque_label = tkinter.Label(self.filewin,text="Torque",font=helv14B,bg="lightgreen").grid(row=4,column=0)
        self.torque_variable= tkinter.Label(self.filewin,text="Torque:",textvariable=self.T,font = helv14B,bg="lightgreen").grid(row=4,column=1)
        self.torque_unit = tkinter.Label(self.filewin,text="Nm",font = helv14B, bg="lightgreen").grid(row=4,column=2)
    
    def calculateT(self):
        self.Axle_Radius = float(self.AR.get())
        self.mass = float(self.Mass.get())
        self.Gforce1 = self.mass*self.g
        self.T1=self.Axle_Radius*self.Gforce1
        self.T.set("%.2f" % self.T1)
    
    
    def gearRatios(self): #Calculates the torque on a motor resulting from a mass tied to a rope around an axle connected to gears
        print ("Calculate torque on motor from gear ratios")
        self.filewin = tkinter.Toplevel(self,bg="lightgreen")
        helv14B = font.Font(family="DejaVu Sans Sans",size=14,weight="bold")
        helv18B = font.Font(family="DejaVu Sans",size=18,weight="bold")
        self.G1_label = tkinter.Label(self.filewin, text="Gear 1 (leave blank if none):", font = helv14B, bg="lightgreen").grid(row=0, column=0)
        self.G1_entry = tkinter.Entry(self.filewin, textvariable=self.G1, font = helv14B)
        self.G1_entry.grid(row=0,column=1)
        self.G1_note = tkinter.Label(self.filewin, text="teeth", font = helv14B, bg="lightgreen").grid(row=0,column=2)
        self.G2_label = tkinter.Label(self.filewin, text="Gear 2 (leave blank if none):", font = helv14B, bg="lightgreen").grid(row=1, column=0)
        self.G2_entry = tkinter.Entry(self.filewin, textvariable=self.G2, font = helv14B)
        self.G2_entry.grid(row=1,column=1)
        self.G2_note = tkinter.Label(self.filewin, text="teeth", font = helv14B, bg="lightgreen").grid(row=1,column=2)
        self.G3_label = tkinter.Label(self.filewin, text="Gear 3 (leave blank if none):", font = helv14B, bg="lightgreen").grid(row=2, column=0)
        self.G3_entry = tkinter.Entry(self.filewin, textvariable=self.G3, font = helv14B)
        self.G3_entry.grid(row=2,column=1)
        self.G3_note = tkinter.Label(self.filewin, text="teeth", font = helv14B, bg="lightgreen").grid(row=2,column=2)
        self.G4_label = tkinter.Label(self.filewin, text="Gear 4 (leave blank if none):", font = helv14B, bg="lightgreen").grid(row=3, column=0)
        self.G4_entry = tkinter.Entry(self.filewin, textvariable=self.G4, font = helv14B)
        self.G4_entry.grid(row=3,column=1)
        self.G4_note = tkinter.Label(self.filewin, text="teeth", font = helv14B, bg="lightgreen").grid(row=3,column=2)
        self.S1_label = tkinter.Label(self.filewin, text="Planetary Stage 1 (leave blank if none):", font = helv14B, bg="lightgreen").grid(row=4, column=0)
        self.S1_entry = tkinter.Entry(self.filewin, textvariable=self.S1, font = helv14B)
        self.S1_entry.grid(row=4,column=1)
        self.S1_note = tkinter.Label(self.filewin, text="teeth", font = helv14B, bg="lightgreen").grid(row=4,column=2)
        self.S2_label = tkinter.Label(self.filewin, text="Planetary Stage 2 (leave blank if none):", font = helv14B, bg="lightgreen").grid(row=5, column=0)
        self.S2_entry = tkinter.Entry(self.filewin, textvariable=self.S2, font = helv14B)
        self.S2_entry.grid(row=5,column=1)
        self.S2_note = tkinter.Label(self.filewin, text="teeth", font = helv14B, bg="lightgreen").grid(row=5,column=2) 
        self.calculate = tkinter.Button(self.filewin,text="Calculate",font = helv14B, bg="lightgreen",command=self.calculateRatio).grid(row=6,column=1)
        self.gearratio_label = tkinter.Label(self.filewin,text="Gear Ratio:",font = helv14B, bg="lightgreen").grid(row=7,column=0)
        self.gearratio_variable = tkinter.Label(self.filewin,textvariable=self.ratio1,font = helv14B, bg="lightgreen").grid(row=7,column=1)
        
        
    def calculateRatio(self):
        #Read the gear data from the form and create the self.gears list
        self.ratio = 1
        if self.G1.get() == "":
            self.Gear1 = 0
        else:
            self.Gear1 = float(self.G1.get())
        if self.G2.get() == "":
            self.Gear2 = 0
        else:
            self.Gear2 = float(self.G2.get())
        if self.G3.get() == "":
            self.Gear3 = 0
        else:
            self.Gear3 = float(self.G3.get())
        if self.G4.get() == "":
            self.Gear4 = 0
        else:
            self.Gear4 = float(self.G4.get())
        self.gears=[]
        if self.Gear1 == 0 or self.Gear2 ==0:
            pass
        else:
            self.gears.append(self.Gear1)
            self.gears.append(self.Gear2)
        if self.Gear3 == 0 or self.Gear4 ==0:
            pass
        else:
            self.gears.append(self.Gear3)
            self.gears.append(self.Gear4)
        #Calculate the gear ratio based on the gears stage:
                #Zero, Two or four gears may be used here.
        if len(self.gears)==4:
            self.ratio = 1.0/(self.gears[0]/self.gears[1]*self.gears[2]/self.gears[3])
        elif len(self.gears)==2:
            self.ratio = 1.0/(self.gears[0]/self.gears[1])
        else:  #Only 0, 2 or 4 gears are acceptable.  Assume no gears if not 2 or 4
            self.ratio = 1.0
        #Further ratio calculations from the planetary gear stage:
        self.Stage1=self.S1.get()
        self.Stage2=self.S2.get()
        self.stages=[] 
        if self.Stage1=="" or self.Stage1=="0":
            pass
        else:
            self.stages.append(int(self.Stage1))
            
        if self.Stage2=="" or self.Stage2=="0":
            pass
        else:
            self.stages.append(int(self.Stage2))
        #print(self.stages)
        #print(self.ratio)
        for i in self.stages:
            self.ratio*=i
        self.ratio1.set("%.2f" % self.ratio)
        
    
    def sim(self):  #This function animates the climbing simulation
        #Create the floor
        self.floor = self.canvas.create_rectangle(self.X_MIN, self.Y_MAX-self.FLOOR_HEIGHT, self.X_MAX,self.Y_MAX, outline='white',fill='black')
        #Create the celing
        self.ceiling = self.canvas.create_rectangle(self.X_MIN, self.Y_MIN, self.X_MAX,self.Y_MIN+self.CEILING_HEIGHT, outline='white',fill='black')
        #Create the robot
        self.robot = []
        for i in range(0,3):
            self.robot.append(self.canvas.create_rectangle(self.X_INIT+i*self.ROBOT_SPACE, self.Y_INIT, self.X_INIT+self.ROBOT_WIDTH+i*self.ROBOT_SPACE, self.Y_INIT+self.ROBOT_HEIGHT, outline='white',fill='blue'))
        height = 0
        for i in range(0,3):
            print (self.RC[i].Climb_Time)
        pixel_height = self.Y_MAX-self.Y_MIN-self.FLOOR_HEIGHT-self.CEILING_HEIGHT-self.ROBOT_HEIGHT
        max_height=0
        while max_height < self.CLIMB_HEIGHT:
            for i in range(0,3):
                self.canvas.delete(self.robot[i])
                if height*0.94/self.RC[self.currentRC].Climb_Time>max_height:
                    max_height=height*0.94/self.RC[self.currentRC].Climb_Time
                self.robot[i] = self.canvas.create_rectangle(self.X_INIT+i*self.ROBOT_SPACE, self.Y_INIT-height*0.94/self.RC[i].Climb_Time, self.X_INIT+self.ROBOT_WIDTH+i*self.ROBOT_SPACE, self.Y_INIT+self.ROBOT_HEIGHT-height*0.94/self.RC[i].Climb_Time, outline='white',fill='blue')
            height +=1
            time.sleep(self.TIME_DELAY)
            self.canvas.update()
    
   
        
         
    #Place holder function - allows the program to work partially
    def donothing(self):
        pass
    
    
    def quit(self):
        app.destroy()

    
        
                
        
        
        



#Main class - calls menubar class
class App(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        menubar = MenuBar(self)
        self.geometry("1600x1000")
        self.title("Climbing Module Simulator")
        self.config(menu=menubar)
        self.configure(background="lightgreen")
        #self.bind_all("<Control-s>", menubar.sim())
        #self.bind_all("<Control-e>", menubar.settings())
        
    

#Start the program:
if __name__ == "__main__":
    app=App()
    app.mainloop()
