'''
16. Ejercicio: Define una función que tome una lista de números y retorne el
número más grande de la lista.
'''
print("Ejercicio_16: función obtiene el máximo de una lista")

lista_numeros=[13,23,12,1,4,56,32,72,65,68,42]
print ("lista: ",lista_numeros)

def maximo(lista_numeros):
      mayor=lista_numeros[0]
      for i in range(len(lista_numeros)):
        if lista_numeros[i]>mayor:
            mayor=lista_numeros[i]
      return mayor

print("el máximo de la lista es: ",maximo(lista_numeros))