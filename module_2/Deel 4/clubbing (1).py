PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

band_kleur = ''

while True:
    leeftijd_persoon = int(input('Hoe oud ben je: '))
    if leeftijd_persoon < 18:
        print("Je bent te jong om hier te komen.")
        print(f'probeer het in {18 - leeftijd_persoon} jaar nog eens')
    if leeftijd_persoon > 18:
        naam_klant = input('Wat is je naam? ')
        if naam_klant in VIP_LIST:
            if leeftijd_persoon >= 21:
                band_kleur = 'blauw'

            if leeftijd_persoon <21:
                band_kleur = 'rood'
            
            print(f'Je krijgt van mij een {band_kleur} band')
        if naam_klant not in VIP_LIST

                



