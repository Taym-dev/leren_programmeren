def vraag_naam_leeftijd():
    naam_persoon = input('Vul uw naam in: ')
    leeftijd_persoon = int(input("Vul uw leeftijd in: "))
    return {"name": naam_persoon, "age": leeftijd_persoon}


gebruiker_info = vraag_naam_leeftijd()
print(gebruiker_info['name'],'is', gebruiker_info['age'],'jaar')