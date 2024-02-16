from random import shuffle

KLEUREN_KAART = ['harten','schoppen','klaver','ruiten']

KAART_GETAL = ['2','3','4','5','6','7','8','9','10','boer','vrouw','aas']

deck = []

for kleur in KLEUREN_KAART:
    for waarde in KAART_GETAL:
        kaart = f"{kleur} {waarde}"
        deck.append(kaart)
deck.append("Joker 1" and "Joker 2")

shuffle(deck)
for i in range(7):
    print(deck[i])
print('\n')
print(deck)