aantal_lijstjes = int(input("Hoeveel lijstjes? "))
 
lijstjes = []
 
for x in range(1, aantal_lijstjes + 1):
    lengte = int(input(f"Hoeveel in lijst {x}? "))
    lijst1 = list(range(x, x * lengte + 1, x))
    lijstjes.append(lijst1)
 
#print(lijstjes)
print(lijstjes)