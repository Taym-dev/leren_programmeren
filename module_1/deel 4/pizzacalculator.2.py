PIZZA_FORMAAT_GROOT = 10.55
PIZZA_FORMAAT_NORMAAL = 10
PIZZA_FORMAAT_KLEIN = 9.55

PIZZA_FORMAAT_KLEIN_FORMAAT = '11 cm 5'
PIZZA_FORMAAT_NORMAAL_FORMAAT = '13 cm 5'
PIZZA_FORMAAT_GROOT_FORMAAT = '16 cm 5'

PIZZA_FORMAAT_LIJST = {'groot','normaal','klein'}

try:
    pizzasklant_hoeveelheid = int(input("Hoeveel pizza's wil je halen?"))
except:
    print('graag een getal invullen !')

else:

    pizzasklant_grote = input('Kies de grote van je pizza (groot) (normaal) (klein): ').lower()

    if pizzasklant_grote not in PIZZA_FORMAAT_LIJST:
        print('voer een formaat in')


    totaal_prijs_groot = pizzasklant_hoeveelheid * PIZZA_FORMAAT_GROOT
    totaal_prijs_normaal = pizzasklant_hoeveelheid * PIZZA_FORMAAT_NORMAAL
    totaal_prijs_klein = pizzasklant_hoeveelheid * PIZZA_FORMAAT_KLEIN


    if pizzasklant_grote in ('groot','Groot'):
        print (f"Je hebt {pizzasklant_hoeveelheid} grote Pizza's van {PIZZA_FORMAAT_GROOT_FORMAAT} in totaal kost het {totaal_prijs_groot}  ")

    elif pizzasklant_grote in ('normaal','Normaal'):
        print (f"Je hebt {pizzasklant_hoeveelheid} normaal Pizza's van {PIZZA_FORMAAT_NORMAAL_FORMAAT} in totaal kost het {totaal_prijs_groot}  ")

    elif pizzasklant_grote in ('klein','Klein'):
        print (f"Je hebt {pizzasklant_hoeveelheid} klein Pizza's van {PIZZA_FORMAAT_KLEIN_FORMAAT} in totaal kost het {totaal_prijs_groot}  ")

