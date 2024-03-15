from RobotArm import RobotArm
 
robotArm = RobotArm("exercise 10")
 
for i in range(5):
    robotArm.grab()
 
    for _ in range(9 - (i * 2)): robotArm.moveRight()
 
    robotArm.drop()
 
    for _ in range(8 - (i * 2)): robotArm.moveLeft()
 
robotArm.wait()