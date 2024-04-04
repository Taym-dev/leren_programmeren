from fruitmand import fruitmand

kleur_vertaling = {
    'yellow': 'gele',
    'green': 'groene',
    'orange': 'oranje',
    'red': 'rode',
    'brown': 'bruine'
}


langste_naam_fruit = max(fruitmand, key=lambda fruit: len(fruit['name']))

vertaalde_kleur = kleur_vertaling.get(langste_naam_fruit['color'], langste_naam_fruit['color'])

print(f"Het fruit met de langste naam is de {vertaalde_kleur} {langste_naam_fruit['name']} met een gewicht van {langste_naam_fruit['weight']} gram.")
