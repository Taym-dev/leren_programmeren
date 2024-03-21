from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

for stapelnummer in range (5):
    robotArm.moveRight()# ga naar stapel 1

    for bloknummer in range(6):#verplaats 6 keer een blokje
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    if stapelnummer < 4:
        robotArm.moveRight()



# robotArm.moveRight()

# for _ in range(6):
#     robotArm.moveRight()
#     robotArm.grab()
#     robotArm.moveLeft()
#     robotArm.drop()

# robotArm.moveRight()
# robotArm.moveRight()

# for _ in range(6):
#     robotArm.moveRight()
#     robotArm.grab()
#     robotArm.moveLeft()
#     robotArm.drop()

# robotArm.moveRight()
# robotArm.moveRight()

# for _ in range(6):
#     robotArm.moveRight()
#     robotArm.grab()
#     robotArm.moveLeft()
#     robotArm.drop()

# robotArm.moveRight()
# robotArm.moveRight()

# for _ in range(6):
#     robotArm.moveRight()
#     robotArm.grab()
#     robotArm.moveLeft()
#     robotArm.drop()




robotArm.wait()