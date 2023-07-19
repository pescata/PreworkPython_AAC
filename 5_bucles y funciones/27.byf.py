'''
27. Ejercicio: Define una función que tome una lista y retorne la lista sin
duplicados.
'''
print("Ejercicio_27: generar lista sin duplicados")

lista=[12,13,14,13,17,16,17,17,18]
print("lista: ",lista)

def lista_sin_duplicados(lista):
    resultado=list(set(lista))
    print("lista sin duplicados: ",resultado)

lista_sin_duplicados(lista)