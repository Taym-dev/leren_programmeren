from fruitmand import fruitmand

totaal_gewicht = 0
for fruit in fruitmand:
    totaal_gewicht += fruit['weight']
print(totaal_gewicht)

watermeloen = {
    'name': 'watermeloen',
    'weight': 3000,  
    'color': 'green',
    'round': True
}
fruitmand.append(watermeloen)

totaal_gewicht_met_watermeloen = 0
for fruit in fruitmand:
    totaal_gewicht_met_watermeloen += fruit['weight']
print(totaal_gewicht_met_watermeloen)