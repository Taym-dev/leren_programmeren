MIN_WEIGHT = 90
MAX_WEIGHT = 120

MIN_HEIGHT = 150
MAX_HEIGHT = 220

MIN_EXP_DIEREN = 4
MIN_EXP_BALLEN = 5
MIN_EXP_ACROOBAAT = 3

geslacht = input("Bent u een man of een vrouw (m/v): ")
heeft_truck_rijbwjis = input("Heeft u een vrachtwagenrijbewijs (j/n): ")
heeft_hooge_hoed = input("Bent u in bezit van een hoge hoed (j/n): ")
gewicht = int(input("Hoe zwaar bent u in KG: "))
lengte = int(input("Hoe lang bent u in CM: "))
hasCertificate = input("Bent u in bezit van het certificaat 'Overleven met gevaarlijk personeel' (j/n): ")
hasExpAnimals = int(input("Hoeveel jaar prakijkervaring heeft u met dieren-dressuur: "))
hasExpBalls = int(input("Hoeveel jaar ervaring heeft u met jongleren: "))
hasExpAcro = int(input("Hoeveel jaar prakijkervaring heeft u met acrobatiek: "))
hasSchool = input("Bent u in bezit van een MBO4 diploma of hoger (j/n): ")
hasExpBusiness = int(input("Hoeveel jaar ervaring heeft u met ondernemen: "))
businesswerknemers = int(input("Hoeveel werknemers had uw bedrijf: "))

if geslacht == "m":
	hasMustache = input("Heeft u een snor breder dan 10CM (j/n): ")
elif geslacht == "v":
	hasHair = input("Heeft u rood krulhaar langer dan 20CM (j/n): ")


if not heeft_truck_rijbwjis == "j":
	print("U heeft een vrachtwagen rijbewijs nodig...")

if not heeft_hooge_hoed == "j":
	print("U heeft een hoge hoed nodig...")

if not gewicht >= MIN_WEIGHT:
	print("U weegt te weinig, 90KG is de ondergrens...")

if not gewicht <= MAX_WEIGHT:
	print("U weegt te veel, 120KG is de grens...")

if not lengte >= MIN_HEIGHT:
	print("U bent te klein, 150CM is de ondergrens...")

if not lengte <= MAX_HEIGHT:
	print("U bent te lang, 220CM is de grens...")

if not (hasExpAnimals >= 4 or hasExpBalls >= 5 or hasExpAcro >= 3):
	print("U mist ervaring met dieren-dresuur (4 jaar), jongleren (5 jaar) of acrobatiek (3 jaar)...")

if not hasSchool:
	print("U heeft een MBO4 diploma of hoger nodig...")

if not hasExpBusiness > 3:
	print("U heeft meer dan 3 jaar ervaring ondernemen nodig...")

if not businesswerknemers >= 5:
	print("Uw bedrijf had/ heeft minimaal 5 werknemers nodig...")

if geslacht == "m" and not hasMustache == "j":
	print("U moet een snor hebben van minimaal 10CM breed...")

if geslacht == "v" and not hasHair == "j":
	print("U moet rood krulhaar hebben van minimaal 20CM...")

if heeft_truck_rijbwjis == "j" and heeft_hooge_hoed == "j" and (gewicht >= MIN_WEIGHT or gewicht <= MAX_WEIGHT) and (lengte >= MIN_HEIGHT or lengte <= MAX_HEIGHT) and hasCertificate == "j" and (hasExpAnimals >= 4 or hasExpBalls >= 5 or hasExpAcro >= 3) and hasSchool and hasExpBusiness > 3 and businesswerknemers >= 5 and ((geslacht == "m" and hasMustache) or (geslacht == "v" and hasHair)):
	print("Gefeliciteerd, je bent aangenomen voor de functie 'Circusdirecteur'")
else:
	print("Helaas, je bent niet aangenomen voor de functie 'Circusdirecteur'")