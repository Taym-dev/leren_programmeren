gastheer = True
drank = True
chips = True

wie_is_de_gastheer = input('Wie is de gastheer? ')

aantal_gasten = int(input('Hoeveel gasten zijn er? '))

if gastheer and aantal_gasten >= 4 and aantal_gasten <= 20 and drank and chips:
    print('Start the Party')
else:
    print('No Party')
