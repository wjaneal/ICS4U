
class Robot:
    def __init__(self,name):
        self.name = name
    def E_Up(self):
        print("Moving Elevator Up")
    def E_Down(self):
        print("Moving Elevator Down")
    def S_Up(self):
        print("Moving Shoulder Up")
    def S_Down(self):
        print("Moving Shoulder Down")
    def Name(self):
        print ("The robot's name is ", self.name)
R = Robot("Aliyah")
R.E_Up()
R.Name()
R.E_Down()
R.Name()
R.S_Down()
R.S_Up()
R.Name()
