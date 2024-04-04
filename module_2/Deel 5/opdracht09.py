from fruitmand import fruitmand

fruitmand.sort(key=lambda fruit: fruit['weight'], reverse=True)

for fruit in fruitmand:
    print(f"{fruit['name']}: {fruit['weight']}")

