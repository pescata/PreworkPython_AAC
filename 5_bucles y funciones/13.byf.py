'''
13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en
orden ascendente.
'''
print("Ejercicio_13: ordenar lista de forma ascendente")

from random import randint
lista=[randint(1,100) for i in range(20)] #crea una lista de 20 números aleatorios del 1 al 100.
print("esta es la lista creada: ",lista)

def orden_lista(lista):
    lista.sort()
    print ("esta es la lista ordenada: ",lista)

orden_lista(lista)