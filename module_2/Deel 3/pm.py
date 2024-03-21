tijd = 0

while tijd < 24:
    tijd += 1

    if tijd < 12:
        print(f"{str(tijd).zfill(2)} am")
    if tijd == 12:
        print('12 pm ')
    if tijd == 24:
        print('12 am')
    elif tijd > 12:
        print(f"{str(tijd - 12).zfill(2)} pm")
