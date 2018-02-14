#coding: utf-8
n = int(input("Escriba un número entero mayor que 1: "))
while n <= 1:
    n = int(input(str(n) + " no es mayor que 1. Inténtelo de nuevo: "))
c = n

print("numeros primos: ", final="")
i=2
while c > 1:
    while c % i == 0:
        c = c // i
        print(i)
   i +=1
print(copia)
print ("programa terminado")
