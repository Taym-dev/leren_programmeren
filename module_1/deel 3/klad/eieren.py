
DOOS_12 = 12
DOOS_6 = 6

aantal_eieren = int(input('Hoeveel eieren wil je?'))

aantal_dozen_12 = aantal_eieren // DOOS_12
resterende_eieren = aantal_eieren % DOOS_12

aantal_dozen_6 = resterende_eieren // DOOS_6
resterende_eieren = resterende_eieren % DOOS_6

if resterende_eieren > 0:
    aantal_dozen_6 += 1


print(f"Je hebt {aantal_dozen_12} van 12 en {aantal_dozen_6} van 6 nodig om {aantal_eieren} eieren in te pakken.")


x = 10
y = 5
if x > y:
    print("A")
if x < y:
    print("B")