'''
32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena
pero con las palabras en orden inverso.
'''
print("Ejercicio_32: función que recibe una cadena y la retorna en orden inverso")
cadena=input("introduce una cadena de texto: ")
print("cadena introducida: ",cadena)

def invertir_cadena(cadena):
  return ' '.join(cadena.split()[::-1])
print("cadena invertida: ",invertir_cadena(cadena))
