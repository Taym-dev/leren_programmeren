from fruitmand import fruitmand

print(fruitmand)


for fruit in fruitmand:
    if fruit['name'] == 'druif':
        fruitmand.remove(fruit) 

kleuren = {}

for fruit in fruitmand:
    if fruit['color'] not in kleuren:
        kleuren.append(fruit['color'])


for kleur in kleuren:
    print(kleur)
