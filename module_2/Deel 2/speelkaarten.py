from random import shuffle

KLEUREN_KAART = ['harten','schoppen','klaver','ruiten']

KAART_GETAL = ['2','3','4','5','6','7','8','9','10','boer','vrouw','koning','aas']

deck = []

for kleur in KLEUREN_KAART:
    for waarde in KAART_GETAL:
        kaart = f"{kleur} {waarde}"
        deck.append(kaart)
deck.append("Joker 1")
deck.append('Joker 2')

shuffle(deck)
print(deck)

for i in range(7):
    print(deck.pop(0))
print(len(deck)) 
