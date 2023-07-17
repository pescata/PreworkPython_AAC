'''
2. Ejercicio: Dado un número, imprime si es par o impar.
'''
print("Ejercicio_2: par vs. impar")

x=int(input("introduce un número: "))
if x==0:
    print(f"el número {x} es igual a cero")
elif x%2==0:
    print(f"el número {x} es un número par")
else:
    print(f"el número {x} es impar")