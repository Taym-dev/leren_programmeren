sex = input("Bent u een man of een vrouw (m/v): ")
hasTruckLicense = input("Heeft u een vrachtwagenrijbewijs (j/n): ")
hasHighHat = input("Bent u in bezit van een hoge hoed (j/n): ")
weight = int(input("Hoe zwaar bent u in KG: "))
height = int(input("Hoe lang bent u in CM: "))
hasCertificate = input("Bent u in bezit van het certificaat 'Overleven met gevaarlijk personeel' (j/n): ")
hasExpAnimals = int(input("Hoeveel jaar prakijkervaring heeft u met dieren-dressuur: "))
hasExpBalls = int(input("Hoeveel jaar ervaring heeft u met jongleren: "))
hasExpAcro = int(input("Hoeveel jaar prakijkervaring heeft u met acrobatiek: "))
hasSchool = input("Bent u in bezit van een MBO4 diploma of hoger (j/n): ")
hasExpBusiness = int(input("Hoeveel jaar ervaring heeft u met ondernemen: "))
businessEmployees = int(input("Hoeveel werknemers had uw bedrijf: "))

if sex == "m":
	hasMustache = input("Heeft u een snor breder dan 10CM (j/n): ")
elif sex == "v":
	hasHair = input("Heeft u rood krulhaar langer dan 20CM (j/n): ")

MIN_WEIGHT = 90
MAX_WEIGHT = 120

MIN_HEIGHT = 150
MAX_HEIGHT = 220

MIN_EXP_ANIMALS = 4
MIN_EXP_BALLS = 5
MIN_EXP_ACRO = 3

if not hasTruckLicense == "j":
	print("U heeft een vrachtwagen rijbewijs nodig...")

if not hasHighHat == "j":
	print("U heeft een hoge hoed nodig...")

if not weight >= MIN_WEIGHT:
	print("U weegt te weinig, 90KG is de ondergrens...")

if not weight <= MAX_WEIGHT:
	print("U weegt te veel, 120KG is de grens...")

if not height >= MIN_HEIGHT:
	print("U bent te klein, 150CM is de ondergrens...")

if not height <= MAX_HEIGHT:
	print("U bent te lang, 220CM is de grens...")

if not (hasExpAnimals >= 4 or hasExpBalls >= 5 or hasExpAcro >= 3):
	print("U mist ervaring met dieren-dresuur (4 jaar), jongleren (5 jaar) of acrobatiek (3 jaar)...")

if not hasSchool:
	print("U heeft een MBO4 diploma of hoger nodig...")

if not hasExpBusiness > 3:
	print("U heeft meer dan 3 jaar ervaring ondernemen nodig...")

if not businessEmployees >= 5:
	print("Uw bedrijf had/ heeft minimaal 5 werknemers nodig...")

if sex == "m" and not hasMustache == "j":
	print("U moet een snor hebben van minimaal 10CM breed...")

if sex == "v" and not hasHair == "j":
	print("U moet rood krulhaar hebben van minimaal 20CM...")

if hasTruckLicense == "j" and hasHighHat == "j" and (weight >= MIN_WEIGHT or weight <= MAX_WEIGHT) and (height >= MIN_HEIGHT or height <= MAX_HEIGHT) and hasCertificate == "j" and (hasExpAnimals >= 4 or hasExpBalls >= 5 or hasExpAcro >= 3) and hasSchool and hasExpBusiness > 3 and businessEmployees >= 5 and ((sex == "m" and hasMustache) or (sex == "v" and hasHair)):
	print("Gefeliciteerd, je bent aangenomen voor de functie 'Circusdirecteur'")
else:
	print("Helaas, je bent niet aangenomen voor de functie 'Circusdirecteur'")