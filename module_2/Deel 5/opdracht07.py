from fruitmand import fruitmand

totaal_gewicht = 0
for fruit in fruitmand:
    totaal_gewicht += fruit['weight']
print(totaal_gewicht)

# Toevoegen van een watermeloen aan de fruitmand
watermeloen = {
    'name': 'watermeloen',
    'weight': 5000,  # Gewicht van de watermeloen
    'color': 'green',
    'round': True
}
fruitmand.append(watermeloen)

# Opnieuw afdrukken van het gewicht van de volledige fruitmand zonder sum
totaal_gewicht_met_watermeloen = 0
for fruit in fruitmand:
    totaal_gewicht_met_watermeloen += fruit['weight']
print(totaal_gewicht_met_watermeloen)