from random import randint

MAXIMAAL_AANTAL_SPEELRONDES = 20
speelrondes = 0
score_gebruiker = 0

while speelrondes < MAXIMAAL_AANTAL_SPEELRONDES:
    print('Je moet een random getal raden tussen 1 en 1000')
    getal_random = randint(1, 1000)
    print(getal_random)
    aantal_speelrondes_in_een_ronde = 0  
    
    while aantal_speelrondes_in_een_ronde < 10:
        gok_persoon_getal = int(input('Raad het getal tussen de 1 en de 1000: '))
        aantal_speelrondes_in_een_ronde += 1
        
        if gok_persoon_getal == getal_random:
            score_gebruiker += 1
            print('Je hebt het goed!')
            print(f'Jouw score is {score_gebruiker}')
            print("\n")
            verder_raden = input('Wil je verder raden? (ja/nee): ').lower()
            if verder_raden != "ja":
                print(f'Dit is je eindscore: {score_gebruiker}')
                break  
        elif aantal_speelrondes_in_een_ronde == 10:
            print("Dit was je laatste poging van deze ronde")
            print(f'Het juiste getal was: {getal_random}')
            print(f'Je hebt een score van {score_gebruiker}')
            break  
        else:
            verschil = abs(gok_persoon_getal - getal_random)
            if verschil < 20:
                print('Je bent heel warm')
            elif verschil < 50:
                print('Je bent warm')
            elif gok_persoon_getal < getal_random:
                print('Hoger!')
            elif gok_persoon_getal > getal_random:
                print('Lager!')
    
    speelrondes += 1





