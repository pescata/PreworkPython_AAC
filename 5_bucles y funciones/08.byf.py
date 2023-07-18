'''
8. Ejercicio: Define una función que tome un número y retorne True si es un
número perfecto, False en caso contrario. Un número perfecto es aquel que es
igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número
perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.
'''
print("Ejercicio_8: función que evalua si un número es perfecto")

n=int(input("introduce el número a evaluar: "))

def num_perfecto(n):
    suma=0
    for i in range(1,n):
        if n%i==0:
           suma+=i
    return suma==n

print(f"¿el número {n} es perfecto?: ",num_perfecto(n))