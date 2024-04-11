#Deze functie kijkt naar gelijken nummers
def gelijken_numbers(getal:int) -> bool:
    return getal % 2 == 0

#Deze functie draait de zin om
def woord_omgedraaid(zin:str) -> str:
    woorden_lijst = zin.split()
    omgedraaide_woorden = woorden_lijst[::-1]
    omgedraaide_zin = ' '.join(omgedraaide_woorden)
    return omgedraaide_zin
#deze function telt elke losse karakter in de zin
def optellen_losse_letters(text:str) -> int:
    unieke_characters_set = set(text)
    unieke_opteller = len(unieke_characters_set)
    return unieke_opteller

#Deze functie checkt voor het gemidelde van de woorden
def gemmidelde_woord_lengte(sentence:str) -> float:
    woorden = sentence.split()
    
    totalen_lengte = 0
    for woord in woorden:
        totalen_lengte += len(woord)

    gemmidelde_lengte = totalen_lengte / len(woorden)
    return gemmidelde_lengte

#deze functie print de keer tafel op basis van je input
def print_keer_tafel(getal:int, aantal_keer:int=10) -> None:
    for keer in range(1, aantal_keer+1):
        resultaat = keer * getal
        print(f'{keer} x {getal} = {resultaat}')
