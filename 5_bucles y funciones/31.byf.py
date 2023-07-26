'''
31. Ejercicio: Define una función que reciba un número entero n y retorne una lista
con los n primeros números primos.
'''
print("Ejercicio_31: función que recibe un número n y retorna lista con los n primeros números primos")

n=int(input("introduzca un número: "))

def num_primo(n):
    if n<=1:
       return False
    for i in range(2,n*n+1):
            if n%i == 0:
                return False
            else:
               return True

def primeros_n_primos(n):
   primos = []
   numero = 2
   while len(primos) < n:
      if num_primo(numero):
         primos.append(numero)
      numero += 1
   print(f"los {n} primeros números primos son: ",primos)

primeros_n_primos(n)