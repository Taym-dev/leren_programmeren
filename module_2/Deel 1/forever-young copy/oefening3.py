from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

for _ in range(4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()

robotArm.wait()