'''
24. Ejercicio: Define una función que tome un número y retorne un diccionario con
la tabla de multiplicar de ese número del 1 al 10.
'''
print("Ejercicio_24: tabla de multiplicar")

n=int(input("introduce un número: "))

def tabla_multiplicar(n):
    resultado={i:n*i for i in range(1,11)}
    print (f"la tabla del {n} es: ",resultado)

tabla_multiplicar(n)