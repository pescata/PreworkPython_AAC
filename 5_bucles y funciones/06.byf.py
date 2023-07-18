
'''
6. Ejercicio: Define una función que tome una lista y un número n, y retorne los
primeros n elementos de la lista.
'''
print("Ejercicio_6: función que devuelve los primeros n elementos de una lista")

n=int(input("introduce el número de elementos: "))

def primeros_n_elementos(lista, n):
  if n>len(lista):
    print("el número indicado supera el número de elementos de la lista")
  else:
    return lista[:n]
print(f"los primeros {n} elementos de la lista son: ",primeros_n_elementos([1, 2, 3, 4, 5, 6, 7], n))

