'''
29. Ejercicio: Define una función que reciba una lista de números y retorne el
promedio de los números en la lista.
'''
print("Ejercicio_29: promedio de una lista")

lista=[12,13,14,13,17,16,17,17,18]
print("lista: ",lista)

def promedio(lista):
  return sum(lista) / len(lista)

print("el promedio de los números de la lista es: ",promedio(lista))