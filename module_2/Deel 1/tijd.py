from time import sleep
for x in range(0,25):
    if x <= 12:
        print(f'Het is nu {x} am')
    else:
        print(f'Het is nu {x} pm')
    sleep(1)

