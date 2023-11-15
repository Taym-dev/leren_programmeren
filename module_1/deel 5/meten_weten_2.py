def get_int(math_operations):
    nr = int(input(f"Voer {math_operations} in: "))
    return nr
 
nr1 = get_int("voer eerste getal in ")
nr2 = get_int("voer tweede getal in ")
 
 
def vergelijk_getallen(nr1:int, nr2:int) -> str:
    if nr1 == nr2:
        return "Beide getallen zijn gelijk"
    elif nr1 > nr2:
        return f"Maximum: {nr1} en minimum: {nr2}"
    else:
        return f"Maximum: {nr2} en minimum: {nr1}"
   
 
Resultaat = vergelijk_getallen(nr1,nr2)
print(Resultaat)