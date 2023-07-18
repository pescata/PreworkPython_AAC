'''
14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y
retorne la lista de palabras que son más largas que n.
'''
print("Ejercicio_14: función que retorna de una lista de palabras aquellas cuya longitud sea mayor a un número n")

lista=input("introduce palabras de una lista separadas por espacios: ").split()
n=int(input("introduce longitud mínima palabras en lista: "))
print("esta es la lista creada: ",lista)

def palabras_mayores(lista,n):
    return [palabra for palabra in lista if len(palabra) > n]
print("lista resultante:",palabras_mayores(lista,n))

palabras_mayores(lista,n)