def robotics(efficiency):

    def mobile_robot():
        print("mobile robots mostly used in the warehouse")
        efficiency()
        print("also has application in healthcare")
    return mobile_robot

@robotics
def arm_robots():
    print("arm robots used for assembly in manufacturing plants")

arm_robots()

