from gegevens_verzamelen import vraag_naam_leeftijd_woonplaats

def verzamel_gegevens():
    gegevens = []
    while True:
        invoer = input("Toets enter om door te gaan of stop om te printen: ")
        if invoer.lower() == 'stop':
            break
        gegevens.append(vraag_naam_leeftijd_woonplaats())
    return gegevens

def print_resultaat(gebruikers_info):
    print("\nResultaat:")
    for info in gebruikers_info:
        print(info['name'], 'is', info['age'], 'jaar oud en woont in', info['city'])

#info['city']       info['name']     info['age']
        
gebruikers_info = verzamel_gegevens()
print_resultaat(gebruikers_info)


def score(dice):
    puntentelling = {1:1000, 6:600, 5:500, 4:400, 3:300, 2:200}
    dobbelsteen_aantallen = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    for worp in dice:
        dobbelsteen_aantallen[worp] += 1

    totaal_punten = 0

    for waarde, aantal in dobbelsteen_aantallen.items():
        if aantal >= 3:
            totaal_punten += puntentelling[waarde] * (aantal // 3)
        if waarde == 1:
            totaal_punten += 100 * (aantal % 3)
        elif waarde == 5:
            totaal_punten += 50 * (aantal % 3)

    return totaal_punten
