def afrond_naar_stuivers(bedrag : float ) -> float:
    CENTEN_OM_AFTERONDEN = 5
    PROCENT = 100
    afgerond_bedrag = round(bedrag * PROCENT/ CENTEN_OM_AFTERONDEN ) * CENTEN_OM_AFTERONDEN / PROCENT
    return afgerond_bedrag
 
BEDRAGEN = [2.24, 13.01, 7.33, 4.56, 10.85]
 
for bedrag in BEDRAGEN:
    afegronde_bedrag = afrond_naar_stuivers(bedrag)
    print(f"echte bedrag : {bedrag} > afgeronde : {afegronde_bedrag}")