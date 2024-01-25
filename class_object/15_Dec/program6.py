class comp:

    def __init__(self, lidar, motor, depthCamera):
        self.lidar = lidar
        self.motor = motor
        self.depthCamera = depthCamera

    def botex(self):
        print(self.lidar)
        print(self.motor)
        print(self.depthCamera)

comp1 = comp(8000,"RPLiDAR", "YDLiDAR")
comp2 = comp(2000,"DC motor", "Encoder Motor")
comp3 = comp(40000,"Intel Realsens d34i", "RoboCam")

comp1.botex()
comp2.botex()
comp3.botex()


