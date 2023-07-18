'''
3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos únicos de la lista original.
'''
print("Ejercicio_3: función que crea una lista con los elementos únicos de una lista inicial")

lista=input("introduce los elementos de la lista separados por espacios: ").split()

print("esta es la lista completa: ",lista)

def elementos_unicos(lista):
    return set(lista)

print("y esta es su lista de elementos únicos: ",elementos_unicos(lista))