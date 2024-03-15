from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

for _ in range (8):
    robotArm.moveRight()

for _ in range (8):
    robotArm.grab()

    if robotArm.scan() == "white":
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
        robotArm.moveLeft()
        
    else:
        robotArm.drop()
        robotArm.moveLeft()


robotArm.wait()