WEEK_DAGEN = ('Maandag','Dinsdag','Woensdag','Donderdag','Vrijdag','Zaterdag','Zondag')

zin_een = 'Alle dagen van de week zijn: '

zin_twee = "Alle werkdagen van de week zijn: "

zin_drie = "Alle weekend dagen zijn: "

zin_vier = "Alle dagen in omgekeerde volgorde zijn:  "

zin_vijf = "Alle werkdagen in omgekeerde volgorde zijn:  "

zin_zes = "Alle weekenden in omgekeerde volgorde zijn:  "



for dag in WEEK_DAGEN:
    zin_een += dag + ', '


for dag in WEEK_DAGEN[:5]: 
    zin_twee += dag +', '

for dag in WEEK_DAGEN[5:7]: 
    zin_drie += dag +', '

for dag in WEEK_DAGEN[7::-1]: 
    zin_vier += dag +', '

for dag in WEEK_DAGEN[4::-1]: 
    zin_vijf += dag +', '

for dag in WEEK_DAGEN[6:4:-1]: 
    zin_zes += dag +', '


print('\n')
print (zin_een)
print('\n')
print(zin_twee)
print('\n')
print(zin_drie)
print('\n')
print(zin_vier)
print('\n')
print(zin_vijf)
print('\n')
print(zin_zes)
print('\n')


fruit = ['appel','bannaan','peer','kers']
fruittext = 'de fruitmant bevat ' + ','.join(fruit) + '.'
print(fruittext)