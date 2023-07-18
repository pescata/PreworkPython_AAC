'''
17. Ejercicio: Define una función que reciba un número y retorne la suma de sus
dígitos al cubo.
'''
print("Ejercicio_17: función que suma los dígitos al cubo de un número")
n=int(input("introduzca un número: "))

def suma_cubos_digitos(n):
  return sum(int(digit)**3 for digit in str(n))
print("la suma de sus digitos al cubo es: ",suma_cubos_digitos(n))