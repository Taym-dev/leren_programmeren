MIN_GEWICHT = 90
MAX_GEWICHT = 120

MIN_LENGTE = 150
MAX_LENGTE = 220

solliciteren_baan = input('Je kunt solliciteren voor de volgende banen. Kies uit de volgende vacatures: circus ')

if solliciteren_baan.lower() == 'circus':
    rijbewijs = input('Ben je in bezit van een vrachtwagen rijbewijs? ').lower()
    if rijbewijs == 'ja':
        hoge_hoed = input('Ben je in bezit van een hoge hoed?  ').lower()
        if hoge_hoed == 'ja':
            gewicht = int(input('Hoeveel weeg je? (kilo)'))
            if MIN_GEWICHT <= gewicht <= MAX_GEWICHT:
                lengte = int(input('Hoe lang ben je? (cm)'))
                if MIN_LENGTE <= lengte <= MAX_LENGTE:
                    certificaat = input('Heb je een certificaat? ').lower()
                    if certificaat == 'ja':
                        ervaring_dieren = int(input('Hoeveel jaar ervaring heb je in deze vakken, praktijkervaring met dieren-dressuur'))
                        ervaring_jongleren = int(input('Hoeveel jaar ervaring heb je in jongleren'))
                        ervaring_acrobatiek = int(input('Hoeveel jaar ervaring heb je in acrobatiek? '))
                        if ervaring_dieren >= 4 or ervaring_acrobatiek >= 3 or ervaring_jongleren >= 5:
                            print('Je kunt doorgaan voor een gesprek.')

else:
    print('Helaas je voldoet niet aan de eisen!')