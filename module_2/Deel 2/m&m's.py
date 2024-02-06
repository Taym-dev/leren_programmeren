# import random


# MNMS_KLEUREN = ('Blauw', 'Oranje', 'Groen','Bruin')

# mnms_hoeveelheid = int(input("Hoeveel M&M's wil je toevoegen"))

# lijst_mnms = []

# def mnms_random():
#     for _ in range (mnms_hoeveelheid):
#         random_kleur = random.choice(MNMS_KLEUREN)
#         lijst_mnms.append(random_kleur)
#     return lijst_mnms

# gevulde_zak = (mnms_hoeveelheid, lijst_mnms)
   
# print(gevulde_zak)

import random

def vul_zak_met_mms(aantal_mms):
    beschikbare_kleuren = ('groen', 'bruin')  # Tuple met beschikbare kleuren
    zak_met_mms = []  # Lege lijst om de M&M's op te slaan

    for _ in range(aantal_mms):
        willekeurige_kleur = random.choice(beschikbare_kleuren)
        zak_met_mms.append(willekeurige_kleur)

    return zak_met_mms

# Vraag de gebruiker om het aantal M&M's
aantal_mms_toevoegen = int(input("Hoeveel M&M's wil je aan de zak toevoegen? "))

# Vul de zak met M&M's
gevulde_zak = vul_zak_met_mms(aantal_mms_toevoegen)

# Toon de inhoud van de zak met M&M's
print("Inhoud van de zak met M&M's:", gevulde_zak)
