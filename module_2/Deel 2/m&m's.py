import random

def mnms_random():
    MNMS_KLEUREN = ('Blauw', 'Oranje', 'Groen','Bruin')
    mnms_hoeveelheid = int(input("Hoeveel M&M's wil je toevoegen"))
    lijst_mnms = []
    for _ in range (mnms_hoeveelheid):
        random_kleur = random.choice(MNMS_KLEUREN)
        lijst_mnms.append(random_kleur)
    gevulde_zak = (mnms_hoeveelheid, lijst_mnms)
    return (gevulde_zak)

print(mnms_random())

