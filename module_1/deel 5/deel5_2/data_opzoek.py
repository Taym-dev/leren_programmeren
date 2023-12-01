# toets_data has name:score combinations separated by a komma
def get_value(data: str, separator: str, position: int) -> str:
   value = data.split(separator) # string splits itself into collection of strings
   if position< len(value):
     return value[position]
   else:
     return None
 
resultaat = get_value('Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7', ",", 0) 
print(resultaat)