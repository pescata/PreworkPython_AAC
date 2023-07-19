'''
20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos de la lista original en orden inverso.
'''
print("Ejercicio_20: función que toma una lista y retorna una nueva lista con los elementos de la lista original en orden inverso")
lista_1=[1,5,7,9,3,5,8,7,4,8,9,10]
print("Lista: ",lista_1)
def reverso_lista(lista_1):
    return lista_1[::-1]

print("resultado: ",reverso_lista(lista_1))