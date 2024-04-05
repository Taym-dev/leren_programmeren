import random

deelnemers = []


def vraag_deelnemers():
    while len(deelnemers) < 3:
        naam = input("voer hier de namen in van de mensen ")
        if naam not in deelnemers:
            deelnemers.append(naam)
        else:
            print("Deze naam zit er al in doe een andere naam ")
       

def trek_lootjes():
    lootjes = deelnemers.copy()
    random.shuffle(lootjes)
    while True:
        lootjes_copy = lootjes.copy()
        for i in range(len(deelnemers)):
            deelnemer = deelnemers[i]
            lootje = lootjes_copy[i]
            if deelnemer == lootje:
                random.shuffle(lootjes)
                break
        else:
            break
    return lootjes


print("Voer de namen van deelnemers in (minimaal 3):")
vraag_deelnemers()

if len(deelnemers) >= 3:
    extra_naam = input("Wil je nog een naam toevoegen? (ja/nee): ")
    if extra_naam.lower() == "ja":
        vraag_deelnemers()

    
    lootjes = trek_lootjes()
    print("Deelnemers en hun lootjes:")
    for i in range(len(deelnemers)):
        deelnemer = deelnemers[i]
        lootje = lootjes[i]
        print(f"{deelnemer}: {lootje}")
