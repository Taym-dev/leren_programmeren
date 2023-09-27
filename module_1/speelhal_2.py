TICKET = 7.45
GELD_P_5MIN_PP = 0.37
GELD_P_1_MIN_PP = GELD_P_5MIN_PP / 1


aantal_mensen = 5
ticket_totaal = TICKET * aantal_mensen
geld_p_5min_pp_totaal = GELD_P_5MIN_PP * 9


geld_p_5min_pp_totaal_1 =  geld_p_5min_pp_totaal * aantal_mensen

totaalprijs = ticket_totaal + geld_p_5min_pp_totaal_1

totaalprijs_1 = round(totaalprijs, 5)

print (f'Dit geweldige dagje-uit met {aantal_mensen} mensen in de Speelhal met 45 minuten VR kost je maar {totaalprijs_1} euro')