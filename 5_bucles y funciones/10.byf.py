'''
10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de
ambas (los elementos que están en las dos listas).
'''
print("Ejercicio_10: función intersección listas")
lista_1=input("introduce los elementos de la lista_1 separados por espacios: ").split()
lista_2=input("introduce los elementos de la lista_2 separados por espacios: ").split()

print("lista_1: ",lista_1)
print("lista_2: ",lista_2)

def interseccion(lista_1,lista_2):
    return list(set(lista_1) & set(lista_2))
print ("lista_intersección: ",interseccion (lista_1,lista_2))

interseccion(lista_1,lista_2)