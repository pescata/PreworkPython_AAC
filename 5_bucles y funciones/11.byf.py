'''
11. Ejercicio: Define una función que tome una cadena y determine si es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''
print("Ejercicio_11: función palíndromo")

palabra=(input("introduce una palabra: "))

def palindromo(palabra):
    palabra=palabra.lower()
    if palabra==palabra[::-1]:
        print("si es palíndromo")
    else:
        print("no es palíndromo")

palindromo(palabra)