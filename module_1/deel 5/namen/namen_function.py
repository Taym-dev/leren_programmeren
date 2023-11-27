naamlijst = []


while True:
    naam = input ('wat is je naam?')
    if naam == 'stop':
        break
    elif naam in naamlijst:
        print('je hebt de naam 2x erin')
        naamlijst.remove(naam)

    naamlijst.append(naam)
    naamlijst.reverse()

for x in naamlijst:
    print (x)

