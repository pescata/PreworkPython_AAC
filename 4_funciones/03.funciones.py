'''
3. Ejercicio: Define una función que tome un número y determine si es primo.
'''
print("Ejercicio_3: función que determina si un número es primo")

n=int(input("introduzca un número: "))
def num_primo(n):
    if n<=1:
       print(f"{n} no es un número primo")
    elif n==2:
       print(f"{n} es un número primo")
    else:
        for i in range(2,n):
            if n%i == 0:
                print(f"{n} no es un número primo")
                return False
            else:
               print(f"{n} es un número primo")
               return True

num_primo(n)