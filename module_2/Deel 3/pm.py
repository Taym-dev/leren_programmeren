teller = 0 

while True:
    teller += 1
    if teller  <= 12:
        print(f'am {teller}')
    
    elif teller >= 12:
        print(f'pm {teller - 12}')
    
    if teller == 24:
        break



