'''
1. Ejercicio: Define una función que tome dos números y retorne su suma.
'''
print("Ejercicio_1: función suma 2 números")

n1=int(input("Introduzca un número: "))
n2=int(input("Introduzca otro número: "))

def suma(n1,n2):
  return n1+n2

resultado=suma (n1,n2)
print(f"El resultado de la suma de {n1} y {n2} es: {resultado}")