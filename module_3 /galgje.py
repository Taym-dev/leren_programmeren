import random

woordenlijst = ['oooo']
woord = random.choice(woordenlijst)
geraden_woord = ['_'] * len(woord)
geraden_letters = set()
fouten_pogingen = 0

MAX_FOUTEN = 6

while True:
    print("huidige woord: " + ' '.join(geraden_woord))
    print("geraden letters: " + ' '.join(geraden_letters))
    
    gok = input("raad een letter: ").lower()
    
    if gok in geraden_letters:
        print("Je hebt deze letter al geraden. Probeer een andere letter.")
        continue

    geraden_letters.add(gok)
    
    if gok in woord:
        for index, letter in enumerate(woord):
            if letter == gok:
                geraden_woord[index] = gok
    else:
        fouten_pogingen += 1
        print(f"fout Je hebt nog {MAX_FOUTEN - fouten_pogingen} pogingen over.")
    
    print("\n")
    
    if '_' not in geraden_woord:
        print(f"Gefeliciteerd! Je hebt het woord geraden: {woord}")
        break
    
    if fouten_pogingen >= MAX_FOUTEN:
        print(f"Helaas, je hebt verloren. Het woord was: {woord}")
        break