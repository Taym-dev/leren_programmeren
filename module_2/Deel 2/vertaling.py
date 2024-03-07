vertaal_dict = {
    "hart": "ingang",
    "grot": "teennagels",
    "Draganthor": "geit",
    "schubben": "waterende",
    "vurige": "golf",
    "ogen": "water",
    "draak": "geit",
    "brulde": "spuwde",
    "spuwde": "golf",
    "vlammenzee": "water",
    "bedreigde": "bedreigde",
    "Rurik": "Rurik",
    "beschermde": "beschermde",
    "krachtig": "krachtig",
    "schild": "zwemvliezen",
    "magie": "plastic"
}

originele_tekst = input("voer je tekst in:  ")
for key,waarde in vertaal_dict.items():
    if key in originele_tekst:
        originele_tekst = originele_tekst.replace(key,waarde)

print("Vertaalde tekst: " + originele_tekst)
