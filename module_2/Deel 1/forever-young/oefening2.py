from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

robotArm.grab()
for _ in range(9):
    robotArm.moveRight()
robotArm.drop()

for _ in range(2):
    robotArm.moveLeft()
robotArm.grab()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()