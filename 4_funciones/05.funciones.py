'''
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa.
'''
print("Ejercicio_5: función que devuelve el reverso de una cadena de texto")

texto=input("introduce una cadena de texto: ")

def reverso(texto):
   return texto[::-1]
print(texto[::-1])