TICKET = 7.45
GELD_P_5MIN_PP = 0.37


aantal_minuten = int(input('Hoeveel minuten wil je spelen'))
aantal_mensen = int(input ('Hoeveel mensen wil je meenemen'))
ticket_totaal = TICKET * aantal_mensen
geld_p_5min_pp_totaal = GELD_P_5MIN_PP * 9


geld_p_5min_pp_totaal_1 =  geld_p_5min_pp_totaal * aantal_mensen

totaalprijs = ticket_totaal + geld_p_5min_pp_totaal_1

totaalprijs_1 = round(totaalprijs, 2)

print (f'Dit geweldige dagje-uit met {aantal_mensen} mensen in de Speelhal met 45 minuten VR kost je maar {totaalprijs_1} euro')