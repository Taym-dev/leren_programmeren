from fruitmand import fruitmand

fruitmand = [fruit for fruit in fruitmand if fruit['name'] != 'druif']

kleuren = set(fruit['color'] for fruit in fruitmand)

for kleur in kleuren:
    print(kleur)
