from fruitmand import fruitmand

while True:
    kleuren_keuze = ('yellow', 'green', 'orange', 'red', 'brown')
    kleur_gebruiken_input = input('Welke kleur kies jij uit (yellow, green, orange, red, brown): ')
    if kleur_gebruiken_input not in kleuren_keuze:
        print(f'{kleur_gebruiken_input} is geen geldige keuze')
        continue
    
    aantal_rond = 0
    aantal_niet_rond = 0
    
    for fruit in fruitmand:
        if fruit['color'] == kleur_gebruiken_input:
            if fruit['round']:
                aantal_rond += 1
            else:
                aantal_niet_rond += 1
    
    verschil = aantal_rond - aantal_niet_rond
    
    if verschil > 0:
        print(f"Er zijn {abs(verschil)} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur_gebruiken_input}")
    elif verschil < 0:
        print(f"Er zijn {abs(verschil)} minder ronde vruchten dan niet ronde vruchten in de kleur {kleur_gebruiken_input}")
    else:
        print(f"Er zijn evenveel ronde vruchten als niet ronde vruchten in de kleur {kleur_gebruiken_input}")
    
    break
