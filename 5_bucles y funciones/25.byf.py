'''
25. Ejercicio: Define una función que tome una cadena y retorne un diccionario
con la cantidad de apariciones de cada caracter en la cadena.
'''
print("Ejercicio_25: contador de caracteres de una cadena")

cadena=input("introduce una cadena de texto: ")

def contador_caracteres(cadena):
    resultado={i:cadena.count(i) for i in cadena}
    print("Resultado: ",resultado)

contador_caracteres(cadena)