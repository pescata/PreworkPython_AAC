'''
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while.
'''
print("Ejercicio_2: imprime números pares bucle while")

n=int(input("introduce un número: "))
print(f"los números pares hasta {n} son: ")
i=2
while i<=n:
    print(i,end=" ")
    i+=2