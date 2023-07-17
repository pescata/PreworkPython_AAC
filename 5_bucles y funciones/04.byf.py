'''
4. Ejercicio: Define una función que tome un número y retorne la suma de sus
dígitos.
'''
print("Ejercicio_4: función que suma los dígitos de un número")

n=int(input("introduzca un número: "))
def suma_valores(n):
    suma=0
    while n>0:
        suma=suma+(n%10)
        n=n//10
    return suma
print(f"la suma de los dígitos de {n} es: ",suma_valores(n))