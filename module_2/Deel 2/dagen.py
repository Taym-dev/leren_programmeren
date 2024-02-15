WEEK_DAGEN = ('Maandag','Dinsdag','Woensdag','Donderdag','Vrijdag','Zaterdag','Zondag')

zin_een = 'Alle dagen van de week zijn: '

zin_twee = "Alle werkdagen van de week zijn: "

zin_drie = "Alle weekend dagen zijn: "

zin_vier = "De werkdagen in omgekeerde volgorde zijn:  "

for dag in WEEK_DAGEN:
    zin_een += dag + ', '


for dag in WEEK_DAGEN[:5]: 
    zin_twee += dag +', '

for dag in WEEK_DAGEN[5:7]: 
    zin_drie += dag +', '

for dag in WEEK_DAGEN[7::-1]: 
    zin_vier += dag +', '

print (zin_een)
print(zin_twee)
print(zin_drie)
print(zin_vier)

