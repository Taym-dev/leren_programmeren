from time import sleep

dagen = 0

naam_streepjes_spel = '''
      ,-~~~-.
    :      (.|
     ".__(  !
          `Taym

'''

print(naam_streepjes_spel)

def start():
    print("Hoi dit is een adveture game")
    print("je wordt wakker in een donkere kamer. er is links een deur en rechts ")
    action = input("Wat doe je? ")

    if action.lower() == "open links deur" or action.lower () =='open links' or action.lower () == 'linker ':
        left_door()
    elif action.lower() == "open rechter deur" or action.lower () == 'rechts':
        right_door()
    else:
        print("Foute input probeer je antwoord te veranderen! Probeer opnieuw.")
   
        start()

def left_door():
    print("Je hebt een schatkist gevonden openen of niet?")
    action = input("ja of nee? ")

    if action.lower() == "ja":
        print("Oke je hebt een kaart")
        if action == 'ja':
            action = input('Je bent naar buiten gegaan, Op je kaart staat er en gemarkeerde plek, Wil je daar heen of een hut maken?').lower()
            if action == 'hut' or 'hut maken':
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


                if action == 'slapen' or 'slaap':
                    dagen = 0
                    dagen += 1
                    print(f'Je bent op dag {dagen}')
                    action = input('nieuwe dag nieuwe kansen Wil je nu naar de gemarkeerde plek?').lower()
                    if action == 'ja':
                        print('Het is nog 2 kilometer lopen')
                        sleep(2)
                        print('je hebt 500 meter gelopen')
                        sleep(2)
                        print('je hebt 1 kilo gelopen')
                        sleep(2)
                        print('je hebt 1.5 kilometer gelopen')
                        sleep(2)
                        print('je hebt 2 meter gelopen')
                        sleep(2)
                        print('je bent er ')
                elif action == 'gemarkeerde plek':
                    print('Het is nog 2 kilometer lopen')
                    sleep(2)
                    print('je hebt 500 meter gelopen')
                    sleep(2)
                    print('je hebt 1 kilo gelopen')
                    sleep(2)
                    print('je hebt 1.5 kilometer gelopen')
                    sleep(2)
                    print('je hebt 2 meter gelopen')
                    sleep(2)
                    print('je bent er, Je bent erg moe!! ')

                    action = input('Wil je de schatkist zoeken of slapen op de grond?')
                    if action == 'slapen':
                        dagen = 0
                        dagen += 1
                        print(f'Dag nummer {dagen}')
                        sleep(1)
                        print(' je gaat nu zoeken naar de schatkist')
                        



                
                
            

            elif action.lower == 'ja' or 'jaa':
                print('je zoekt naar de schat kist ')
                

            
            else:
                print('Helaas je gaat het niet halen als je niks wilt doen')


    elif action.lower() == "nee":
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