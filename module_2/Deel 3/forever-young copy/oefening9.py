from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')


for stappen in range(1, 5):
    for _ in range(stappen):
        robotArm.grab()
        for _ in range(5): 
            robotArm.moveRight()
        robotArm.drop()
        for _ in range(5): 
            robotArm.moveLeft()
 
    robotArm.moveRight()





    
    
    


robotArm.wait()