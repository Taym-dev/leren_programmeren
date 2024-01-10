from garage import auto_lijst

print(f"ik heb {len(auto_lijst)} autos in mijn garage")

aantal_toyotas = 0

# for auto in auto_lijst:
#     if auto["merk"] == "Toyota":
#         print(auto)
#         aantal_toyotas += 1

# print (aantal_toyotas)


for motorinhoud in auto_lijst:
    if motorinhoud["motorinhoud"]:
        kleinste_motor = min(motorinhoud.values())
        print (motorinhoud)


print (aantal_toyotas)

    