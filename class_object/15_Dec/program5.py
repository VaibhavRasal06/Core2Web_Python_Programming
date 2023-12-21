
class Robot:

    robot_type = "autonomous mobile robot"

    def __init__(self):
        self.robotCompany = "Rigbetel"
        self.robotPrice = 50000
        self.robotOS = "Ubuntu"

    def robot_details(self):
        print(self.robotCompany)
        print(self.robotPrice)
        print(self.robotOS)
        print(self.robot_type)

info = Robot()
info.robot_details()
print(info.robotPrice)
