'''
3. Ejercicio: Define una función que tome un número y determine si es primo.
'''
print("Ejercicio_3: función números primos")

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
