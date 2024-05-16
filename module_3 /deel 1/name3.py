def vraag_naam_leeftijd_woonplaats():
    naam_persoon = input('Vul uw naam in: ')
    leeftijd_persoon = int(input("Vul uw leeftijd in: "))
    woonplaats_persoon = input("Vul uw woonplaats in: ")
    return {"name": naam_persoon, "age": leeftijd_persoon, "city": woonplaats_persoon}

def verzamel_gegevens():
    gegevens = []
    while True:
        invoer = input("Toets enter om door te gaan of stop om te printen: ")
        if invoer.lower() == 'stop':
            break
        gegevens.append(vraag_naam_leeftijd_woonplaats())
    return gegevens

gebruikers_info = verzamel_gegevens()

print("\nResultaat:")
for info in gebruikers_info:
    print(info['name'], 'is', info['age'], 'jaar oud en woont in', info['city'])
