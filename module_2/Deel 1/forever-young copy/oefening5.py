from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

for _ in range(7):
    robotArm.moveRight()

for _ in range(7):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()



robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.moveLeft()
robotArm.wait()