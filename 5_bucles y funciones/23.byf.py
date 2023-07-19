'''
23. Ejercicio: Define una función que encuentre el elemento más común en una
lista.
'''
print("Ejercicio_23: función que encuentra el elemento más común en una lista")

lista=[12,12,12,36,57,57,98,12,47,56,8,17,72]
print("lista: ",lista)

def elemento_mas_repetido(lista):
    resultado=max(set(lista),key=lista.count)
    print("el elemento más común es: ",resultado)

elemento_mas_repetido(lista)