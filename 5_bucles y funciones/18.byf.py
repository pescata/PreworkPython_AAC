'''
18. Ejercicio: Define una función que reciba una lista de números y retorne el
segundo número más grande de la lista.
'''
print("Ejercicio_18: función que reciba una lista de números y retorne el segundo número más grande de la lista")

lista=[13,27,17,18,21,23,45]
print("Esta es la lista de números: ",lista)

def segundo_maximo(lista):
  lista.sort()
  lista.reverse()
  lista.pop(0)
  print("el segundo valor máximo de la lista es: ",lista[0])

segundo_maximo(lista)