'''
1. Ejercicio: Define una función que tome dos números y retorne su suma.
'''
print("Ejercicio_1: función suma 2 números")

n1=int(input("Introduzca un número: "))
n2=int(input("Introduzca otro número: "))

def suma(n1,n2):
  return n1+n2

resultado=suma (n1,n2)
print("El resultado de la suma es:",resultado)
print(f"El resultado de la suma es: {resultado}")
# se han presentado 2 alternativas de print con diferente sintaxis, pero ambas funcionan correctamente ¿Cúal se debería considerar más eficiente?