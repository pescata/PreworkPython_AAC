'''
1. Ejercicio: Define una función que utilice un bucle para imprimir los primeros n
números de la serie de Fibonacci.
'''
print("Ejercicio_1: función serie Fibonacci con bucle")

def fib(n):
    pen=0
    ult=1
    if n==1:
        print(f"la serie de Fibonacci de {n} elementos es: ",(0))
    elif n==2:
        print(f"la serie de Fibonacci de {n} elementos es: ",(0,1))
    else:
        for i in range(n):
          nuevo=pen+ult
          pen=ult
          ult=nuevo
          print(0,1,nuevo, end=" ")

n=int(input("introduce un número: "))
if n<=0:
    print("este número no es válido para genera la serie fibonacci")
else:
    fib(n)
