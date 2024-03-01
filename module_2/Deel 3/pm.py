tijd = 0

for _ in range(23):
    tijd += 1
    if  tijd <= 12:
        print(f'am {tijd}')
    if  tijd >= 12: 

        print(f'pm {tijd - 11}')