from time import sleep

teller = 31

while True:
    teller += -1 
    sleep(1)
    print(teller)
    if teller == 0:
        print('raket gelanceerd')
        break

