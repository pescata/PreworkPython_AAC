'''
1. Ejercicio: Define una función que tome dos números y retorne su suma.
'''
n1=int(input("Introduzca un número: "))
n2=int(input("Introduzca otro número: "))

def suma(n1,n2):
  return n1+n2

resultado=suma (n1,n2)
print("El resultado de la suma es:",resultado)
print(f"El resultado de la suma es: {resultado}")
# se han presentado 2 alternativas de print con diferente sintaxis, pero ambas funcionan correctamente ¿Cúal se debería considerar más eficiente?


'''
2. Ejercicio: Define una función que tome un número y retorne su factorial.
'''
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

'''
3. Ejercicio: Define una función que tome un número y determine si es primo.
'''
n=int(input("introduzca un número: "))
def num_primo(n):
    if n<=1:
       print(f"{n} no es un número primo")
    elif n==2:
       print(f"{n} es un número primo")
    else:
        for i in range(2,n):
            if n%i == 0:
                print(f"{n} no es un número primo")
                return False
            else:
               print(f"{n} es un número primo")
               return True

num_primo(n)

'''
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos.
'''
n1=int(input("introduce un número: "))
n2=int(input("introduce un número: "))
n3=int(input("introduce un número: "))
n4=int(input("introduce un número: "))
n5=int(input("introduce un número: "))

lista=[n1,n2,n3,n4,n5]

def suma_lista(lista):
   return sum(lista)

print("la suma de los elementos de la lista es: ",suma_lista(lista))

'''
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa.
'''
texto=input("introduce una cadena de texto: ")
print(texto)

def reverso(texto):
   return texto[::-1]
print(texto[::-1])
