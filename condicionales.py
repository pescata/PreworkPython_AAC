'''
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
'''
x=-2
if x>0:
    print("x es positivo")
elif x<0:
    print("x es negativo")
else:
    print("x es igual a cero")

'''
2. Ejercicio: Dado un número, imprime si es par o impar.
'''
x=46
if x==0:
    print("x es igual a cero")
elif x%2==0:
    print("x es un número par")
else:
    print("x es impar")
'''
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
'''
a=71
b=72
c=72
if a>b:
    if a>c:
        print("el máximo es:",a)
    else:
        print("el máximo es:",c)
elif b>a:
    if b>c:
        print("el máximo es:",b)
    else:
        print("el máximo es:",c)
else:
    print("el máximo es:",c)

# ejercicios condicionales completados