'''
34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de
letras vocales en la cadena.
'''
print("Ejercicio_34: función que cuenta las vocales de una cadena de texto")
cadena=input("introduce una cadena de texto: ")

def contar_vocales(cadena):
  return sum(1 for c in cadena.lower() if c in 'aeiou')
print(contar_vocales(cadena))