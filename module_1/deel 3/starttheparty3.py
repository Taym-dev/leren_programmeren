naam_gastheer = input("Naam van de gastheer?  ").lower()
gastheer = len(naam_gastheer) > 0
aantal_gasten = int(input('Hoeveel gasten zijn er?')).lower()
gasten_ok = aantal_gasten > 4 and aantal_gasten <20
drank = True
chips = True
jouw_naam = "Taym? "
slb_naam = "eugene " 
 
feest = (gastheer == jouw_naam) or (gasten_ok and drank and chips and naam_gastheer != slb_naam) or (gastheer and drank and naam_gastheer != slb_naam)
 
#Feest1 = (gastheer == slb_naam) and gasten_ok < 3 or gasten_ok > 20 == False
 
 
if feest:
    print("Start the Party")
else:
    print("No Party")