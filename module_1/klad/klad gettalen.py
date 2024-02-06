GETALLEN_REEKS = (2, 7, 15, 25, 24, 28, 17, 420, 8, 3, 20)

for number in GETALLEN_REEKS:
    if number % 2 == 0 and number > 12:
        number = len(number)
        print(number)


