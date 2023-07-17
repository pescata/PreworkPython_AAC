'''
2. Ejercicio: Define una función que tome un número y retorne una lista de sus
divisores.
'''
print("Ejercicio_2: función que determina los divisores de un número y los devuelva en una lista")

n=int(input("introduce un número: "))
def divisores (n):
    resultado=[i for i in range(1,n+1) if n%i==0]
    return resultado

if n<=0:
    print("Esta función no calcula divisores de números menores o iguales a cero")
else:
   print(f"los divisores de {n} son: ",divisores(n))