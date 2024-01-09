from time import sleep

dagen = 0

naam_streepjes_spel = '''
      ,-~~~-.
    :      (.|
     ".__(  !
          `Taym

'''

print(naam_streepjes_spel)


def merging():
    action = input('Wil je de schatkist zoeken!').lower()
    if action == 'ja':
        action = input('Waar wil je gaan zoeken op het strand of in het bos!').lower()
        if action == 'bos':
            print('In het wilde')
            sleep(0.2)
            print('Het bos waar mensen verwijderen')
            sleep(0.2)
            print('Je hebt twee boomstammen gevonden, Je maakt nu die boomstammen aan elkaar en gaat het water op ')
            sleep(0.5)
            print('Gefeliciteerd , Mensen hebben je gezien op het water Je hebt het overleefd')
        elif action == 'strand' or action == 'strand':
            print("Op het strand vind je een aangestrande boot die kapot is")
            sleep(0.3)
            print('Om de boot te repareren kost het je 1 boomstam ')
            sleep(0.3)
            action = input('Wil je het bos in?')
            if action == 'ja':
                print('Je hebt twee boomstammen gevonden neem er eentje mee!')
                sleep(0.2)
                print('repareer je boot nu')
                sleep(2)
                print('je boot is af, Je gaat nu het water op')
                sleep(0.3)
                print('Gefeliciteerd je bent aangemeerd op een vissers eiland!')
            else: 
                print('Je hebt het niet gehaald en je verhongerd')
                start()
        else:
            print("Foute input probeer je antwoord te veranderen! Probeer opnieuw.")
            start()

    else:
        print("Je hebt het niet gehaald .")

def start():
    print("Hoi dit is een adveture game")
    print("je wordt wakker in een donkere grot. er is links een gang en rechts een gang ")
    action = input("Welke kant kies je ? ").lower()

    if action == "links" or action =='open links' or action == 'linker ':
        left_door()
    elif action == "open rechter deur" or action == 'rechts':
        right_door()
    else:
        print("Foute input probeer je antwoord te veranderen! Probeer opnieuw.")
        start()

def left_door():
    print("Je hebt een schatkist gevonden openen of niet?")
    action = input("ja of nee? ")

    if action.lower() == "ja" and action != 'nee':
        print("Oke je hebt een kaart")
        if action == 'ja':
            action = input('Je bent naar buiten gegaan, Op je kaart staat er en gemarkeerde plek, Wil je naar de gemarkeerde plek of een hut bouwen?').lower()
            if action == 'hut' or action == 'hut maken':
                print('je gaat een hut bouwen')
                print('je bent begonnen met bouwen')
                sleep(2)
                print('je hebt 20 procent af')
                sleep(2)
                print('je hebt 40 procent af')
                sleep(2)
                print('je hebt 60 procent af')
                sleep(2)
                print('je hebt 80 procent af')
                sleep(3)
                print('je hebt je hut gebouwd')
                action = input('Wil je slapen of naar de gemarkeerde plek op je map').lower()

                if action == 'slapen' or action == 'slaap':
                    dagen = 0
                    dagen += 1
                    print(f'Je bent op dag {dagen}')
                    action = input('nieuwe dag nieuwe kansen Wil je nu naar de gemarkeerde plek?').lower()
                    if action == 'ja':
                        print('Het is nog 2 kilometer lopen')
                        sleep(2)
                        print('je hebt 500 meter gelopen')
                        sleep(2)
                        print('je hebt 1 kilometer gelopen')
                        sleep(2)
                        print('je hebt 1.5 kilometer gelopen')
                        sleep(2)
                        print('je hebt 2 kilometer gelopen')
                        sleep(2)
                        print('je bent er ')
                        merging()
            elif action == 'gemarkeerde plek' or action == 'gemarkeerdepleka':
                print('Het is nog 2 kilometer lopen')
                sleep(2)
                print('je hebt 500 meter gelopen')
                sleep(2)
                print('je hebt 1 kilometer gelopen')
                sleep(2)
                print('je hebt 1.5 kilometer gelopen')
                sleep(2)
                print('je hebt 2 kilometer gelopen')
                sleep(2)
                print('je bent er, Je bent erg moe!! ')

                action = input('Wil je de schatkist zoeken of slapen op de grond?')
                if action == 'slapen':
                    dagen = 0
                    dagen += 1
                    print(f'Dag nummer {dagen}')
                    sleep(1)
                    print(' je gaat nu zoeken naar de schatkist')
                    merging()
                else:
                    print('Helaas je hebt het niet gehaald!')
                    start()
            else:
                print('Helaas je gaat het niet halen als je niks wilt doen')

    elif action.lower() == "nee" and action != 'ja':
        print("Je hebt de deur dicht gemaakt en je gaat naar huis.")

    else:
        print("Foute input probeer je antwoord te veranderen! Probeer opnieuw.")
        left_door()

def right_door():
    print("Je bent in een gas kamer ga snel weg!")

    sleep(4)
    print ('je bent dood')
    print('-'* 173)
    start()

start()
