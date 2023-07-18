'''
5. Ejercicio: Define una función que tome una cadena y cuente el número de
vocales en la cadena.
'''
print("Ejercicio_5: función que cuenta el número de vocales de una cadena")

cadena=input("introduce una cadena de texto: ")

def contar_vocales(cadena):
  return sum(1 for letra in cadena if letra.lower() in 'aeiou')
print(f"en la cadena introducida hay {contar_vocales(cadena)} vocales")
