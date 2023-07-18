'''
15. Ejercicio: Define una función que tome un número y calcule su serie de
Fibonacci.
'''
print("Ejercicio_1: función serie Fibonacci")

def fib(n):
    pen=0
    ult=1
    for i in range(n):
        nuevo=pen+ult
        print(pen, end=" ")
        pen=ult
        ult=nuevo

n=int(input("introduce el número de elementos de la serie de Fibonacci: "))
if n<=0:
    print("el número de elementos debe ser mayor que 0")
elif n==1:
    print(f"la serie de Fibonacci de {n} elementos es: ",0)
elif n==2:
    print(f"la serie de Fibonacci de {n} elementos es: ",0,1)
else:
    print(f"la serie de Fibonacci de {n} elementos es: ", end="")
    fib(n)