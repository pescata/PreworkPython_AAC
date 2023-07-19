'''
22. Ejercicio: Define una función que reciba una lista de números y retorne la
suma acumulada de los números
'''
print("Ejercicio_23: función que recibe una lista de números y retorna la suma acumulada de los números")

lista=[12,36,57,98,12,47,56,8,17,72]
print("lista: ",lista)

def suma_acumulada(lista):
    suma=0
    suma_acumulada=[]
    for i in lista:
        suma+=i
        suma_acumulada.append(suma)
    return suma_acumulada

print("lista acumulada: ",suma_acumulada(lista))