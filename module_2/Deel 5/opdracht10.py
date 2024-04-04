from fruitmand import fruitmand

# fruitmand.sort(key=lambda fruit: fruit['weight'], reverse=True)

def mijnfunctie(fruit):
    return fruit['weight']


fruitmand.sort(key=mijnfunctie, reverse=True)



for fruit in fruitmand:
    print(f"{fruit['name']}: {fruit['weight']}")

