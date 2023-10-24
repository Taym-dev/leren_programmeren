MIN_GEWICHT = 90
MAX_GEWICHT = 120

MIN_LENGTE = 150
MAX_LENGTE = 220
ANTWOORDEN = ('ja', 'Ja', 'JA', "j")


solliciteren_baan = input('Je kunt solliciteren voor de volgende banen. Kies uit de volgende vacatures: circus ')
rijbewijs = input('Ben je in bezit van een vrachtwagen rijbewijs? ').lower()
hoge_hoed = input('Ben je in bezit van een hoge hoed?  ').lower()
gewicht = int(input('Hoeveel weeg je? (kilo)'))
lengte = int(input('Hoe lang ben je? (cm)'))
certificaat = input('Heb je een certificaat? ').lower()
ervaring_dieren = int(input('Hoeveel jaar ervaring heb je in deze vakken, praktijkervaring met dieren-dressuur'))
ervaring_jongleren = int(input('Hoeveel jaar ervaring heb je in jongleren'))
ervaring_acrobatiek = int(input('Hoeveel jaar ervaring heb je in acrobatiek? '))
#

if (solliciteren_baan == 'nee' or (lengte < MIN_LENGTE and lengte > MAX_LENGTE) or rijbewijs == 'nee' or hoge_hoed == 'nee' or (gewicht < MIN_GEWICHT and gewicht > MAX_GEWICHT)):
    resultaat_sollicitatie = ('Je bent niet aangenomen')
    print(f"Hallo , u bent {resultaat_sollicitatie}aangenomen.")


elif (ervaring_dieren < 4) and (ervaring_jongleren < 5) and (ervaring_acrobatiek < 3):
    resultaat_sollicitatie = 'Je bent niet aangenomen'
else:
    resultaat_sollicitatie = 'Je bent aangenomen'


print (resultaat_sollicitatie)