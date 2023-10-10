a = int(input("Voer het eerste gehele getal voor (a) in: "))
b = int(input("Voer het tweede gehele getal voor (b) in: "))

if a > b:
    Max = a
    Min = b
    print(f'a is het grootste getal: {Max}')
elif a < b:
    Max = b
    Min = a
    print(f'b is het grootste getal: {Max}')
else:
    print('a en b zijn even groot')

print(f'Het minimum is: {Min}')
print(f'Het maximum is: {Max}')