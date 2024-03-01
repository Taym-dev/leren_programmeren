def vertaal_tekst(tekst, vertaal_dict):
    woorden = tekst.split()
    vertaalde_tekst = []

    for woord in woorden:
        if woord in vertaal_dict:
            vertaalde_tekst.append(vertaal_dict[woord])
        else:
            vertaalde_tekst.append(woord)

    return ' '.join(vertaalde_tekst)

def main():
    vertaling = {
        'hart': 'ingang',
        'grot': 'grot',
        'Draganthor': 'Draganthor',
        'glinsterende': 'glinsterende',
        'schubben': 'teennagels',
        'vurige': 'waterende',
        'ogen': 'ogen',
        'draak': 'geit',
        'brulde': 'brulde',
        'spuwde': 'spuwde',
        'vlammenzee': 'golf',
        'hen': 'hen',
        'bedreigde': 'bedreigde',
        'Rurik': 'Rurik',
        'beschermde': 'beschermde',
        'krachtig': 'krachtig',
        'schild': 'zwemvliezen',
        'magie': 'plastic'
    }

    input_tekst = input("Voer een stukje tekst in: ").lower()
    vertaalde_tekst = vertaal_tekst(input_tekst, vertaling)

    print("\nVertaalde tekst:")
    print(vertaalde_tekst)

if __name__ == "__main__":
    main()
