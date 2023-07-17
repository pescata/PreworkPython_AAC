'''
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
'''
print("Ejercicio_1: positivo vs. negativo")

x=int(input("introduce un número: "))
if x>0:
    print(f"el número {x} es positivo")
elif x<0:
    print(f"el número {x} es negativo")
else:
    print(f"el número {x} no es ni positivo ni negativo")