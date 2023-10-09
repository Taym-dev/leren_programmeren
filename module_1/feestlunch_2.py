CROISSANTJES = 0.39

STOKBROOD = 2.78

KORTINGSBON = 0.50

aantal_croissantjes = 17
aantal_stokbrood = 2
aantal_kortingsbonnen = 3

croissantjes_totaal =  aantal_croissantjes * CROISSANTJES
stokbrood_totaal = aantal_stokbrood * STOKBROOD
kortingsbon_totaal = aantal_kortingsbonnen * KORTINGSBON

totaal = croissantjes_totaal + stokbrood_totaal - kortingsbon_totaal

print (f'De feestlunch kost je bij de bakker {totaal} euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn')