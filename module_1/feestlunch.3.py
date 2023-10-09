CROISSANTJES = 0.39

STOKBROOD = 2.78

KORTINGSBON = 0.50

aantal_croissantjes = int(input('Hoeveel croissantjes wil je? '))
aantal_stokbrood = int(input('Hoeveel stokbroden wil je? '))
aantal_kortingsbonnen = int(input('Hoeveel kortingsbonnen heb je? '))

croissantjes_totaal =  aantal_croissantjes * CROISSANTJES
stokbrood_totaal = aantal_stokbrood * STOKBROOD
kortingsbon_totaal = aantal_kortingsbonnen * KORTINGSBON

totaal = croissantjes_totaal + stokbrood_totaal - kortingsbon_totaal

afgeronde_totaal = round(totaal ,2)

print (f'De feestlunch kost je bij de bakker {afgeronde_totaal} euro voor de {aantal_croissantjes} croissantjes en de {aantal_stokbrood} stokbroden als de {aantal_kortingsbonnen} kortingsbonnen nog geldig zijn')     