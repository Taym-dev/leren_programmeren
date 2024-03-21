aantal_keer_geantwoord = 0

while True:
    vraag = input('hoe voel je je? (QUIT) om te stoppen: ').lower()
    aantal_keer_geantwoord += 1
    if vraag == 'quit':
        # print(f'Je bent gestopt je hebt de vraag {aantal_keer_geantwoord -1}x beantwoord')
        break

print(f'Je bent gestopt je hebt de vraag {aantal_keer_geantwoord -1}x beantwoord')
