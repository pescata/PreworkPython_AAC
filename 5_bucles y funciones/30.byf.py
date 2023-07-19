'''
30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la
cadena más larga en la lista.
'''
print("Ejercicio_30: función que recibe una lista de cadenas y retorna la cadena más larga")

lista_cadenas=["avalancha","elefante","larguisima","corta","esternocleidomastoideo"]
print("lista: ",lista_cadenas)

def cadena_mas_larga(lista_cadenas):
  return max(lista_cadenas, key=len)

print("la cadena más largad de la lista es: ",cadena_mas_larga(lista_cadenas))

