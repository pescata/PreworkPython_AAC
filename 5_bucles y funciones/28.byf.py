'''
28. Ejercicio: Define una función que reciba un número entero positivo y retorne la
suma de los cuadrados de todos los números pares menores o iguales a ese
número.
'''
print("Ejercicio_28: suma cuadrados números pares")

n=int(input("introduce un número entero: "))

def suma_cuadrados_pares(n):
    return sum(i**2 for i in range(2, n+1, 2))

print(f"la suma de los cuadrados de los números pares hasta {n} es: ",suma_cuadrados_pares(n))