from functions import *
LIJST_LETTERS = ('a','b','c','d')
print("A) getallen optellen")
print("B) getallen aftrekken")
print("C) getallen vermenigvuldigen")
print("D) getallen delen")
print("E) getallen ophogen")
print("F) getallen verlagen")
print("G) getallen verdubbelen")
print("H) getallen halveren")
print('I) u verlaat het programma')
print('\n')

while True:
    choice = input('Kies: ').lower()

    if choice in LIJST_LETTERS:
        n1 = float(input('uw eerste getal = '))
        n2 = float(input('uw tweede getal = '))
    
    if choice == 'i':
        print('u bent gestopt')
        break

    if choice == 'a':
        result = addition(n1, n2)
        print(f'uw antwoord is: {n1} + {n2} = {result}')

    elif choice == 'b':
        result = subtraction(n1, n2)
        print(f'uw antwoord is: {n1} - {n2} = {result}')

    elif choice == 'c':
        result = multiplication(n1, n2)
        print(f'uw antwoord is: {n1} x {n2} = {result}')

    elif choice == 'd':
        result = division(n1, n2)
        print(f'uw antwoord is: {n1} : {n2} = {result}')

    elif choice == 'e':
        n1 = float(input('Uw eerste getal: '))
        n2 = input('Uw tweede getal (druk op Enter als u 1 wilt gebruiken): ')
        
        if n2.strip() == '':
            n2 = 1
        else:
            n2 = float(n2)
            
        result = n1 + n2
        print(f'uw antwoord is: {n1} + {n2} = {result}')

    elif choice == 'f':
        n1 = float(input('Uw eerste getal: '))
        n2 = input('Uw tweede getal (druk op Enter als u -1 wilt gebruiken): ')
        
        if n2.strip() == '':
            n2 = 1
        else:
            n2 = float(n2)
            
        result = n1 - n2
        print(f'uw antwoord is: {n1} - {n2} = {result}')

    elif choice == 'g':
        n1 = float(input('Uw eerste getal: '))
        n2 = input('Uw tweede getal (druk op Enter als u x2 wilt gebruiken): ')
        
        if n2.strip() == '':
            n2 = 2
        else:
            n2 = float(n2)
            
        result = n1 * n2
        print(f'uw antwoord is: {n1} x {n2} = {result}')

    elif choice == 'h':
        n1 = float(input('Uw eerste getal: '))
        n2 = input('Uw tweede getal (druk op Enter als u :2 wilt gebruiken): ')
        
        if n2.strip() == '':
            n2 = 2
        else:
            n2 = float(n2)
            
        result = n1 / n2
        print(f'uw antwoord is: {n1} : {n2} = {result}')

    while True:
        print("\nNu komt de volgende berekening!")
        print(f"Wil je wat met de uitkomst ({result}) doen?")
        print("A) iets optellen")
        print("B) iets aftrekken")
        print("C) met iets vermenigvuldigen")
        print("D) ergens door delen")
        print("E) ophogen")
        print("F) verlagen")
        print("G) verdubbelen")
        print("H) halveren")
        print("I) niets")
        print('\n')
        
        next_choice = input('Kies: ').lower()

        if next_choice == 'i':
            print('u bent gestopt')
            break
        elif next_choice in 'abcdefgh':
            n1 = result
            if next_choice in 'abcd':
                n2 = float(input('uw tweede getal = '))
            elif next_choice == 'e':
                n2 = 1
            elif next_choice == 'f':
                n2 = 1
            elif next_choice == 'g':
                n2 = 2
            elif next_choice == 'h':
                n2 = 2
            
            if next_choice == 'a':
                result = addition(n1, n2)
                print(f'uw antwoord is: {n1} + {n2} = {result}')

            elif next_choice == 'b':
                result = subtraction(n1, n2)
                print(f'uw antwoord is: {n1} - {n2} = {result}')

            elif next_choice == 'c':
                result = multiplication(n1, n2)
                print(f'uw antwoord is: {n1} x {n2} = {result}')

            elif next_choice == 'd':
                result = division(n1, n2)
                print(f'uw antwoord is: {n1} : {n2} = {result}')

            elif next_choice == 'e':
                result = n1 + n2
                print(f'uw antwoord is: {n1} + {n2} = {result}')

            elif next_choice == 'f':
                result = n1 - n2
                print(f'uw antwoord is: {n1} - {n2} = {result}')

            elif next_choice == 'g':
                result = n1 * n2
                print(f'uw antwoord is: {n1} x {n2} = {result}')

            elif next_choice == 'h':
                result = n1 / 2
                print(f'uw antwoord is: {n1} : 2 = {result}')
        else:
            print("Ongeldige keuze, probeer opnieuw.")
