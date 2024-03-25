boodschappenlijst = {}
doorgaan = ""

while doorgaan.lower() != 'nee':
    artikel_klant_keuze = input('Welk artikel wilt u toevoegen? ')
    aantal_artikel_klant_keuze = int(input(f'Hoeveel {artikel_klant_keuze} wilt u? '))
    if artikel_klant_keuze in boodschappenlijst:
        boodschappenlijst[artikel_klant_keuze] += aantal_artikel_klant_keuze
    else:
        boodschappenlijst[artikel_klant_keuze] = aantal_artikel_klant_keuze
    doorgaan = input("Wilt u nog een artikel toevoegen? (ja/nee) ")
    

print("Uw boodschappenlijst:")
# for artikel, aantal in boodschappenlijst.items():
#     print(f"{aantal}x {artikel}")

for key in boodschappenlijst:
    print(key,boodschappenlijst[key])

