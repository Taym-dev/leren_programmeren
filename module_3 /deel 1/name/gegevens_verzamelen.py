# gegevens_verzamelen.py

def vraag_naam_leeftijd_woonplaats():
    naam_persoon = input('Vul uw naam in: ')
    leeftijd_persoon = int(input("Vul uw leeftijd in: "))
    woonplaats_persoon = input("Vul uw woonplaats in: ")
    return {"name": naam_persoon, "age": leeftijd_persoon, "city": woonplaats_persoon}
