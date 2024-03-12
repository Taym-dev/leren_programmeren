from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

robotArm.grab()
for _ in range (4):
    robotArm.moveRight()
robotArm.drop()
for _ in range (3):
    robotArm.moveLeft()
robotArm.grab()
for _ in range(4):
    robotArm.moveRight()
robotArm.drop()
for _ in range(4):
    robotArm.moveLeft()
robotArm.grab()
for _ in range(4):
    robotArm.moveRight()
robotArm.drop()





robotArm.wait()