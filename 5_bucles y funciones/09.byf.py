'''
9. Ejercicio: Define una función que reciba un número y retorne su
representación en binario.
'''
print("Ejercicio_9: función para conversión de número decimal a binario")

n=int(input("introduce el numero que quieres convertir a binario: "))
def DecBin(n):
    d=[]
    print(f"el número {n}",end=" ")
    while n>=1:
        d.append(n%2)
        n=n//2
    s=d[::-1]
    print("se corresponde con el binario:",s,end=" ")

DecBin(n)