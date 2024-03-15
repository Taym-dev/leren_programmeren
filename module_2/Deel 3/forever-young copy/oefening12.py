from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

for _ in range (8):
    robotArm.moveRight()

for i in range(8):
    robotArm.grab()

    if robotArm.scan() == 'red':
        for i in range(i + 1): robotArm.moveRight()
        robotArm.drop()
        for _ in range(i + 2): robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveLeft()

robotArm.wait()