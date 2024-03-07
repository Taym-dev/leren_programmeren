tijd = 0

while True:
    tijd += 1
    if tijd == 24:
        break 
    if tijd <= 12:
        print(f"am {tijd}")
    elif tijd >= 12:
        print(f"pm {tijd - 12}")