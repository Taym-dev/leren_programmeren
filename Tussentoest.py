
#opdracht 1
# for getal in range(1,14):
#     eind_resultaat =  1 * getal
#     print(f"{getal} x {1} = {eind_resultaat}")

#
# for getal in range(1,14): 
#     eind_resultaat =  2 * getal
#     print(f"{getal} x {1} = {eind_resultaat}")

#opdracht 2

lijst_getallen = [5,12,19,27,3] # dit is een list met een list kan je appenden

lijst_getallen.append(25)


print(len(lijst_getallen))

lijst_getallen.remove(12)

print(lijst_getallen)

eerste_getal = lijst_getallen.pop(0)

lijst_getallen.insert(0, 36) #append werkte niet wat append is niet specifiek op de juist locatie zeggen

# print(lijst_getallen)

intotaal = 0

for totaal in lijst_getallen:
    if totaal > 10:
        intotaal += totaal 

print(intotaal)
# lijst_getallen.clear()
# print(lijst_getallen)

# for i in range(1, 4):
#     lijst_getallen.append(i)
# print(lijst_getallen)

# for i in range(4, 51):
#     lijst_getallen.append(i)
# print(lijst_getallen)

# print(lijst_getallen.index(25))

# print(lijst_getallen)
# eerste_element = lijst_getallen.pop(0)
# laatste_element = lijst_getallen.pop(-1)
# lijst_getallen.insert(0, laatste_element)
# lijst_getallen.append(eerste_element)
# print(lijst_getallen)

# lijst_twee = [1, "aap",2 , "apen", 3 ,"watermeloen",15,27,15,"lekker bezig","6" ]

# aantal_int = 0

# for i in lijst_twee:
#     if isinstance(i, int):
#         aantal_int += 1

# print("antal ints = ", aantal_int)
