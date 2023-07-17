'''
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos.
'''
print("Ejercicio_4: función suma números de una lista")

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
