def bereken_BTW(bedrag_ex: float) -> float:
    bedrag_1_incl = bedrag_ex * 1.21
    return bedrag_1_incl



bedrag_1 = 100.00
bedrag_2 = 83.00
bedrag_3 = 71.25
bedrag_1_incl = bereken_BTW(bedrag_1)


print (bedrag_1_incl)