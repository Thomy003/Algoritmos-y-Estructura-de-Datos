from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
  vuelos_copy: List[Tuple[str, str]] = vuelos.copy()
  actual_location: str = origen
  number_of_flights: int = 0
  repeticion: bool = True

  if actual_location != destino:
    while actual_location != destino and repeticion:
      repeticion = False
      for trips in vuelos_copy:
        if actual_location in trips[0]:
          repeticion = True
        else:
          pass
            
      for vuelos in vuelos_copy:
        if actual_location in vuelos[0]:
          actual_location = vuelos[1]
          vuelos_copy.remove(vuelos)
          number_of_flights += 1 
        else:
          pass
    
    if repeticion == False:
        return -1
    else:
        return number_of_flights
  else:
    return -1

if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))