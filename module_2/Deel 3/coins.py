coinValues = [500, 200, 100, 50, 20, 10, 5, 2, 1] # Lijst met values van het geld

toPay = int(float(input('Amount to pay: ')) * 100) # Hier word gevraag hoeveel de klant moest betalen
paid = int(float(input('Paid amount: ')) * 100) #  hier word gevraagt  hoeveel er al betaald is
change = paid - toPay # hier word berekent  wat nog over blijft als wissel geld

geldterug = {} # Dictionary om geld wat je hebt terug gegeven opteslaan

while change > 0 and len(coinValues) > 0: # zolang de change groter dan 0 is en er meer dan 0 coins zijn

  coinValue = coinValues.pop(0) #  hij pakt het eerste element de lijst word steeds kleiner
  nrCoins = change // coinValue # hij kijkt hoeveel het erin past

  if nrCoins > 0: # 
    print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # 
    nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # 
    change -= nrCoinsReturned * coinValue # 
    geldterug[coinValue] = nrCoinsReturned # Het aantal teruggegeven munten toevoegen aan de dictionary

if change > 0: # 
  print('Change not returned: ', str(change) + ' cents') # 
else:
  print('done')

#printen van het geld wat terug gegeven is 
print("geld terug :")
for coin in geldterug:
    count = geldterug[coin]
    print(f"In totaal {count} keer {coin} cent teruggegeven.")

