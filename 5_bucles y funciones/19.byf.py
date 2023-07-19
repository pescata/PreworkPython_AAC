'''
19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al
menos un miembro en común, de lo contrario, retorne False.
'''
print("Ejercicio_19: función que toma dos listas y retorna True si tienen al menos un miembro en común, de lo contrario, retorne False.")

lista_1=[1,5,7,9,3,5,8,7,4,8,9,10]
lista_2=[45,87,82]
print("lista_1: ",lista_1)
print("lista_2: ",lista_2)

def elemento_comun(lista_1,lista_2):
    conjunto_1=set(lista_1)
    conjunto_2=set(lista_2)
    return bool (conjunto_1 & conjunto_2)

resultado=elemento_comun(lista_1,lista_2)
print("el resultado es: ",resultado)
