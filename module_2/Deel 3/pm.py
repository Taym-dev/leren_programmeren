tijd = 0

while True:
    tijd += 1

    if tijd < 12:
        print(f"am {tijd}")
    if tijd == 12:
        print(f'pm {tijd} ')
    if tijd == 24:
        print(f'am {tijd - 12}')
    elif tijd > 12:
        print(f"pm {tijd - 12}")
    if tijd == 24:
        break 