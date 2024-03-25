from random import randint

getal = 0
MAXIMAAL_AANTAL_SPEELRONDES = 20
speelrondes = 0
aantal_speelrondes_in_een_ronde = 0
score_gebruiker = 0


while True:
    print('Je moet een random getal raden tussen 1 en 1000')
    getal_random = randint(1,1000) 
    print(getal_random)
    gok_persoon_getal = int(input('Raad het getal tussen de 1 en de 1000: '))
    aantal_speelrondes_in_een_ronde += 1
    if gok_persoon_getal ==  getal_random:
        score_gebruiker += 1
        print('Je hebt het goed')
        print(f'Jouw score is', {score_gebruiker})
        print("\n")
        verder_raden = input('wil je verder raden?').lower()
        if verder_raden != "ja":
            print(f'Dit is je eind score {score_gebruiker}')
            break
    elif aantal_speelrondes_in_een_ronde >= 10:
        print("Dit was je laatste poging")
        print(f'Je hebt een score van {score_gebruiker}')
        speelrondes += 1
        
    






