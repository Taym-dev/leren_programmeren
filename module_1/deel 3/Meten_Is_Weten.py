a = int(input("vul het eerste hele getal voor (a) in: "))
b = int(input("vul het tweede hele getal voor (b) in: "))

if a > b:
    Max = a
    Min = b
    print(f'getal a is het grootste getal: {Max}')
elif a < b:
    Max = b
    Min = a
    print(f'getal b is het grootste getal: {Max}')
else:
    Max = a
    Min = b
    print('getal a en b getal zijn even groot')

print(f'Het minimum is: {Min}')
print(f'Het maximum is: {Max}')