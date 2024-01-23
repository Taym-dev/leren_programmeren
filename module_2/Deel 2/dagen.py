WEEK_DAGEN = ('Maandag','Dinsdag','Woensdag','Donderdag','Vrijdag','Zaterdag','Zondag')

WEEK_DAGEN_REVERSE = list(WEEK_DAGEN)

WEEK_DAGEN_REVERSE.reverse()

WERK_DAGEN = WEEK_DAGEN[0:5]

WERK_DAGEN_REVERSED = list(WERK_DAGEN)

WERK_DAGEN_REVERSED.reverse()

VRIJE_DAGEN = WEEK_DAGEN[5:7]

VRIJE_DAGEN_REVERSED = list(VRIJE_DAGEN)

VRIJE_DAGEN_REVERSED.reverse()
print(WEEK_DAGEN)
print('--'* 5)
print (WERK_DAGEN)
print('--'* 5)
print(VRIJE_DAGEN)
print('--'* 5)
print(WERK_DAGEN_REVERSED)
print('--'* 5)
print(WEEK_DAGEN_REVERSE)
print('--'* 5)
print(VRIJE_DAGEN_REVERSED)


