n = int(input("Escriba un número entero mayor que 1: "))
while n <= 1:
    n = int(input(str(n) + " no es mayor que 1. Inténtelo de nuevo: "))
copia = n

print("numeros primos: ", final="")
for i in range(2, n + 1):
    while copia % i == 0:
        copia = copia // i
        print(i, end=" ")
print("Programa terminado")
