ticket = 7.45
geld_p_5min_pp = 0.37

ticket_totaal = ticket * 4
geld_p_5min_pp_totaal = geld_p_5min_pp * 9


geld_p_5min_pp_totaal_1 =  geld_p_5min_pp_totaal * 4

totaalprijs = ticket_totaal + geld_p_5min_pp_totaal_1

totaalprijs_1 = round(totaalprijs, 5)

print (f'Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar {totaalprijs_1} euro')