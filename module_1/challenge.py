PRIJS_OLLIEBOLLEN = 99
PRIJS_10_OLLIEBOLLEN = 750
AANTAL_OLIEBOL = 12
hoeveel_10 = AANTAL_OLIEBOL // 10
hoeveel_1 = AANTAL_OLIEBOL % 1
print(hoeveel_10)


PRIJS_APPELFLAP = 149
AANTAL_APPELFLAP = 2


totaal_oliebol = AANTAL_OLIEBOL % 10 * PRIJS_OLLIEBOLLEN + AANTAL_OLIEBOL // 10 * PRIJS_10_OLLIEBOLLEN 
totaal_appelflap = AANTAL_APPELFLAP * PRIJS_APPELFLAP
totaal_bedrag = totaal_oliebol = totaal_appelflap


print(f'Totaal{totaal_oliebol/ 100}')
#print(f'Totaal{totaal_appelflap/ 100}')
#print(f'Totaal{totaal_bedrag/ 100}')