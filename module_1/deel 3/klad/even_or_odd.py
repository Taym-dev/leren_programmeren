def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
gevraagde_getal = int(input('Welke getal wil je '))

print(even_or_odd(gevraagde_getal))

