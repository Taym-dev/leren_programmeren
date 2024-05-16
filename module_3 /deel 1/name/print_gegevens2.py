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
        print(f"In {info['city']} woont de {info['age']} jarige {info['name']}")

gebruikers_info = verzamel_gegevens()
print_resultaat(gebruikers_info)
