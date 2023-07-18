'''
12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para
múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de
cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco
imprima “FizzBuzz”.
'''
print("Ejercicio_12: programa que cambia nombre múltiplos")

for i in range(1,51):
    if i%3==0 and i%5==0:
        print("FizzBuzz",end=" ")
    elif i%3==0:
        print("Fizz",end=" ")
    elif i%5==0:
        print("Buzz",end=" ")
    else:
        print(i,end=" ")