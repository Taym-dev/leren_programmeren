from fruitmand import fruitmand

fruitmand = [fruit for fruit in fruitmand 
                if fruit['name'] != 'druif']

kleuren = set(fruit['color'] for fruit in fruitmand)

# Druk alle verschillende kleuren af
print("Alle verschillende kleuren in de fruitmand zijn:")
for kleur in kleuren:
    print(kleur)
