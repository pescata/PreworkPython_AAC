'''
7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de
letras mayúsculas y minúsculas en la cadena.
'''
print("Ejercicio_7: función que devuelve número de mayúsculas y minúsculas de una cadena de texto")

cadena=input("introduce una cadena de texto: ")

def may_min(cadena):
  n_may = sum(1 for letra in cadena if letra.isupper())
  n_min = sum(1 for letra in cadena if letra.islower())
  return n_may,n_min
print("el número de mayúsculas y minúsculas es respectivamente: ",may_min(cadena))