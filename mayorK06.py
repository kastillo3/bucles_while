#coding: utf-8
x = float(input("Escriba el valor límite: "))
while x <= 0:
    x = float(input("El límite debe ser mayor que 0. Inténtelo de nuevo: "))

numero = float(input("Escriba un número: "))
suma = 0
suma += numero

while suma < x:
    numero = float(input("Escriba otro número: "))
    suma += numero
print("Programa terminado")

