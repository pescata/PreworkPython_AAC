'''
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
'''
print("Ejercicio_3: número mayor")

a=int(input("introduce un número: "))
b=int(input("introduce otro número: "))
c=int(input("introduce un tercer número: "))
if a>=b:
    if a>=c:
        print("el máximo es:",a)
    else:
        print("el máximo es:",c)
elif b>=a:
    if b>=c:
        print("el máximo es:",b)
    else:
        print("el máximo es:",c)
else:
    print("el máximo es:",c)