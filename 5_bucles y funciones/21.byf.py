'''
21. Ejercicio: Define una función que reciba una cadena y cuente el número de
dígitos y letras que contiene.
'''
print("Ejercicio_21: función que recibe una cadena y cuenta su número de digitos y letras")

cadena=input("introduce cadena: ")

def num_dig_letras(cadena):
    dig = sum(i.isdigit() for i in cadena)
    letras = sum(i.isalpha() for i in cadena)
    print (f"la cadena contiene {dig} dígitos y {letras} letras")

num_dig_letras(cadena)