'''
26. Ejercicio: Define una función que tome dos listas y retorne la lista de
elementos que no están en ambas listas.
'''
lista_1=[1,2,3,4,5,6,7,8,9]
lista_2=[2,4,6,8,9]
print("lista_1: ",lista_1)
print("lista_2: ",lista_2)

def eltos_distintos (lista_1,lista_2):
    return list(set(lista_1) ^ set(lista_2))
print("la lista de elementos distintos es: ",(eltos_distintos(lista_1,lista_2)))

eltos_distintos (lista_1,lista_2)