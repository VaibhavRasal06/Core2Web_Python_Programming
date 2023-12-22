def Robotics(autonomous):

    def ROS():
        print("Robot operating on ROS system")
        autonomous()
        print("SLAM is key component in the ROS")
    return ROS

def Automation():
    print("PLC is main component in the Automation industry")

effi = Robotics(Automation)
effi()

