import random

kleuren = ['harten', 'klaveren', 'schoppen', 'ruiten']
waarden = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'boer', 'vrouw', 'heer', 'aas']
deck = [(waarde, kleur) for kleur in kleuren for waarde in waarden] + [('joker', '1'), ('joker', '2')]

#random.shuffle(deck)
random.shuffle(deck)

hand = deck[:7]
overige_kaarten = deck[7:]

print("de bovenste 7 kaarten:")
for kaart in hand:
    print(f"{kaart[0]} van {kaart[1]}")
print("\n"*2)
print("\nOverige kaarten in het deck:")
for kaart in overige_kaarten:
    print(f"{kaart[0]} van {kaart[1]}")
