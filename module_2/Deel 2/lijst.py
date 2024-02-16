def lijst_generator():
    aantal_lijsten = int(input("Hoeveel lijstjes? "))

    alle_lijsten = []
    for i in range(1, aantal_lijsten + 1):
        lengte = int(input(f"hoeveel wil je in je lijstje {i}"))

        lijsten_nu = []
        for j in range(1, lengte + 1):
            lijsten_nu.append(i * j)

        alle_lijsten.append(lijsten_nu)

    return alle_lijsten

resultaat = lijst_generator()
print(resultaat)

