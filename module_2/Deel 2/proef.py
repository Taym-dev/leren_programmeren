totaal = 0

while True:
    try:
        getal_klant = int(input("Voer een getal in: "))
        totaal += getal_klant
        stoppen = input("Wil je stoppen? ja nee : ")
        
        if stoppen == 'ja':
            print("Het totaal van de ingevoerde getallen is:", totaal)
            break
    except ValueError:
        print("Doe opnieuw")