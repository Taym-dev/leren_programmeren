groen = 0 
rijp = 1
rot = 2

appels = [groen, rijp, rijp, rot, groen, rot, rijp, rijp, rot, rijp, groen]

groene_appels = []
for appel in appels:
    if appel == groen:
        appels.pop(appel)

aantal_rijp = appels.count(rijp)
aantal_rot = appels.count(rot)

appels = [appel for appel in appels if appel != rot]

aantal_totaal = len(appels)

percentage_rijp = (aantal_rijp / aantal_totaal) * 100

print("{:.0f}%".format(percentage_rijp))
