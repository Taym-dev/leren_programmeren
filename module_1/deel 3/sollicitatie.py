MIN_GEWICHT = 90
MAX_GEWICHT = 120

MIN_LENGTE = 150
MAX_LENGTE = 220






solliciteren_baan = input('Je kan solliciteren voor de volgende banen. Kies uit de volgende vacaturen: circus ')

if solliciteren_baan == 'circus':
    rijbewijs =input ('ben je in bezit van een vrachtwagen rijbewijs? ')
    if rijbewijs == 'ja':
        hoge_hoed = input('Ben je in bezit van een hoge hoed?  ')
        if hoge_hoed == 'ja':
            gewicht = int(input('Hoeveel weeg je? (kilo)'))
            if gewicht >= MIN_GEWICHT and gewicht <= MAX_GEWICHT:
                lengte= int(input('Hoe lang ben je? (cm)'))
                if lengte >= MIN_LENGTE and lengte <= MAX_LENGTE:
                    certificaat = input('Heb je een certificaat? ')
                    if certificaat == 'ja':
                        ervaring_dieren = int(input('Hoeveel jaar ervaring heb je in deze vakken, praktijkervaring met dieren-dressuur'))
                        ervaring_jongeleren = int(input('Hoeveel jaar ervaring heb je in jongeleren'))
                        ervaring_acrobatiek =  int(input('Hoeveel jaar ervaring heb je in acrobatiek? '))
                        if ervaring_dieren >= 4 or ervaring_acrobatiek >= 3 or ervaring_jongeleren >= 5:
                            print('Je kan doorgaan voor een gesprek. ')