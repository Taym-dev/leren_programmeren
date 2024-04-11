import random

deelnemers = []


def vraag_deelnemers():
    naam = input("voer hier de namen in van de mensen ")
    if naam not in deelnemers:
        deelnemers.append(naam)
    else:
        print("Deze naam zit er al in doe een andere naam ")
       

def trek_lootjes():
    lootjes = deelnemers.copy()
    random.shuffle(lootjes)
    while True:
        oke = True
        for i in range(len(deelnemers)):
            deelnemer = deelnemers[i]
            lootje = lootjes[i]
            if deelnemer == lootje:
                random.shuffle(lootjes)
                oke = False
        if oke == True:
            return lootjes


print("Voer de namen van deelnemers in minimaal 3:")


while True:
    vraag_deelnemers()
    if  len(deelnemers) >= 3:
        extra_naam = input("Wil je nog een naam toevoegen? ja/nee: ")
        if extra_naam.lower() != 'ja':
            break




lootjes = trek_lootjes()
for i in range(len(deelnemers)):
    deelnemer = deelnemers[i]
    lootje = lootjes[i]
    print(f"{deelnemer}: {lootje}")
