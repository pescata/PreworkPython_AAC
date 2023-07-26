'''
35. Ejercicio: Define una función que reciba un número entero y retorne True si es
un número primo, de lo contrario retorne False.
'''
print("Ejercicio_35: función que identifica con true or false si un número es primo")

n=int(input("introduzca un número: "))
def num_primo(n):
    if n<=1:
       return False
    elif n==2:
       return True
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
            else:
               return True

print(num_primo(n))