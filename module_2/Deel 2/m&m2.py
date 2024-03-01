import random


kleuren = ["rood", "blauw", "groen", "geel", "bruin"]


aantal_mms = int(input("Hoeveel M&M's wil je toevoegen aan de zak? "))


zak_met_mms = {}
for _ in range(aantal_mms):
    kleur = random.choice(kleuren)
    if kleur in zak_met_mms:
        zak_met_mms[kleur] += 1
    else:
        zak_met_mms[kleur] = 1

for kleur, aantal in zak_met_mms.items():
    print(f"{kleur} {aantal}")
