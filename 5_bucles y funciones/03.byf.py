'''
3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos únicos de la lista original.
'''
print("Ejercicio_3: función que crea una lista con los elementos únicos de una lista inicial")

lista=[1,3,5,65,3,7,9,4,8,6,5,2,12,5,23,65,9,5,2,12,4,1,2,"alberto","lia","lia","lia", "nico","nico","emilia","ana"]

print("esta es la lista completa: ",lista)

def elementos_unicos(lista):
    return set(lista)

print("esta es la lista de elementos únicos de la lista anterior: ",elementos_unicos(lista))
