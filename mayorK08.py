#coding: utf-8
numero = int(input("Escriba un número par: "))
while numero %2!= 0:
    numero = int(input(str(numero) + " no es un número par. Inténtelo de nuevo: "))
contador = 1
r = input("¿Quiere escribir otro número par? (SI/NO) ")

while r == "SI":
    numero = int(input("Escriba un número par: "))
    while numero %2!= 0:
        numero = int(input(str(numero) + " no es un número par. Inténtelo de nuevo: "))
    contador += 1
    r = input("¿Quiere escribir otro número par? (SI/NO) ")

print()
if contador == 0:
    print("No ha escrito ningún número par")
elif contador == 1:
    print("Ha escrito 1 número par")
else:
    print("Ha escrito", contador, "números pares.")
print("Programa terminado")
