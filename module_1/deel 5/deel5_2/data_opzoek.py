
def get_value(data: str, separator: str, position: int) -> str:
   waarden = data.split(separator) 
   if position > -1 and position < len(waarden) and len(waarden) > 0:
     return waarden[position]
   else:
     return None
 
resultaat = get_value('Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7', ",", 9) 
print(resultaat)