n = int(input("Escriba un número entero mayor que 1: "))
while n <= 1:
    n = int(input(str(n) + " no es mayor que 1. Inténtelo de nuevo: "))
c = n

print("numeros primos: ", final="")
for i in range(2, n + 1):
    while c % i == 0:
        c = c // i
        print(i, final=" ")
print("Programa terminado")
