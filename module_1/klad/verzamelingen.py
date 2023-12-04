# mijn_lijst = []
# persoon = {}

# for _ in range(3):
#     persoon['voornaam'] = input('wat is uw voornaam')
#     persoon['achternaam'] = input('wat is uw achternaam')
#     mijn_lijst.append(persoon)

# print (mijn_lijst[1]['voornaam'])
# mijn_lijst = []

# autos_info = {}
# for _ in range(2):
#     autos_info['Merk'] = input('Wat is de merk van uw auto: ')
#     autos_info['Prijs'] = int(input('Wat is de prijs van uw auto'))
#     autos_info['Model'] = input('Welke model is uw auto')
#     autos_info.append(mijn_lijst)

# print(mijn_lijst['Prijs'])

mijn_lijst = []

for _ in range(5):
    autos_info = {}  
    autos_info['Merk'] = input('Wat is de merk van uw auto: ')
    autos_info['Prijs'] = int(input('Wat is de prijs van uw auto: '))
    autos_info['Model'] = input('Welke model is uw auto: ')
    mijn_lijst.append(autos_info)  

for autos_info in (mijn_lijst):
    print(autos_info['Prijs'])



