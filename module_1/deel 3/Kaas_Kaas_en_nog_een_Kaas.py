gele_kaas = input('is kaas geel? ')
if gele_kaas == 'nee' :
    blauwe_schimmel = input('Heeft de kaas blauwe schimmel')

    if blauwe_schimmel == 'nee' :
        korst = input('Heeft de kaas korst')
        if korst =='ja' :
            print('Het is Blue de rochban')
        if korst == 'nee':
            print('Het is Foume dambert')

    if blauwe_schimmel == 'ja' :
        korst1 = input('Heeft de kaas korst')

        if korst1 =='ja':
            print('Het is camembert')
        if korst1 == 'nee':
            print('het is Mozzarella')

if gele_kaas == 'ja':
    gaten = input('Zitten er gaten in? ')

    if gaten == 'ja':
        duur = input('Is de kaas belachelijk duur? ')

        if duur == 'ja':
            print('Het is Emmenthaler')
        if duur == 'nee':
            print('het is leerdammer')

    if gaten == 'nee':
        hardheid = input('is de kaas keihard? ')

        if hardheid == 'ja':
            print('Het is Parmigiano Reggiano')
        if hardheid == 'nee':
            print('Het is Goudse kaas')