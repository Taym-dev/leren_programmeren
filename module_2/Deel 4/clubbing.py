PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30
 
DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')
kleuren = ("blauw" , "rood")
 


leeftijd_klant = int(input("hoe oud ben je? "))

if leeftijd_klant >= 18:
    naam_klant = input("wat is je naam ? ").lower()
    if naam_klant in VIP_LIST and leeftijd_klant >=21 :
        print("je krijgt blauw bandje ")
        band_vip = True
        kleur = "blauw"
    elif naam_klant in VIP_LIST and leeftijd_klant < 21 :
        print("je krijgt rood bandje ")
        band_vip = True
        kleur = "rood"
    elif naam_klant  not in VIP_LIST and leeftijd_klant >=21:
        print("je krijgt van mij stempel")
        band_vip = False
        stempel = True
    elif naam_klant  not in VIP_LIST and leeftijd_klant <21:
        band_vip = False
        stempel = False
    drinken = input("wat wil je drinken ? 'cola', 'bier', 'champagne' ").lower()
    if band_vip is True and kleur == "blauw" and drinken in DRANKJES:
        print("alsjeblieft complimenten ")
    elif drinken not in DRANKJES:
        print("sorry geen idee wat je bedoelt hier is een glasje water ")
    elif band_vip is True and kleur == "rood" and drinken in DRANKJES:
        if drinken == "cola" or "bier":
            print("Alstublieft complimenten van het huis ")
        elif drinken == 'champagne':
            print("sorry je mag geen alcohol drinken onder 21")
        else:
            print("hier is een glas water ")
    elif band_vip is  False and stempel is True: 
        if drinken == "cola":
            print(f"het wordt {PRIJS_COLA}")
        elif drinken =="bier":
            print(f"het wordt {PRIJS_BIER}")
        elif drinken == 'champagne':
            print("sorry alleen vip kan champagne halen ")
        else:
            print("ik snap het niet hier is een glas met water ")
    elif  band_vip is  False and stempel is False:
        if drinken == "cola":
            print(f"het wordt {PRIJS_COLA}")
        elif drinken =="bier":
            print("Je mag geen alchohol te drinken als je onder de 21 bent ")
        elif drinken =="champagne":
            print(f"allen vip mogen champagne en onder 21 mag je geen alcohol propeer het in 2025 ")
else:
    print(f"je mag niet naar binnen probeer het in {18 - leeftijd_klant} jaar")