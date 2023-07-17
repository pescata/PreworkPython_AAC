'''
2. Ejercicio: Define una función que tome un número y retorne su factorial.
'''
print("Ejercicio_2: función factorial")

n=int(input("introduzca un número: "))

def factorial (n):
    if n<0:
       print("no es posible calcular el factorial de un número negativo")
    elif n==0 or n==1:
       print(f"el factorial de {n} es: 1")
    else:
        resultado = 1
        i = 1
        while (i<=n):
           resultado = resultado * i
           i = i + 1
        print (f"el factorial de {n} es: {resultado}")

factorial(n)