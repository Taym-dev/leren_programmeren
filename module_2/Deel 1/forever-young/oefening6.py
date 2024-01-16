from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

robotArm.moveRight()


for _ in range (3):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()

    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()

robotArm.wait()