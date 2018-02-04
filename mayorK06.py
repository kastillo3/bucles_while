#coding: utf-8
x=float(input("introduce un numero:"))
cont=0
suma=0
while (x<=0):
    x=float(input("Error, introduce otro:"))
while (x>cont): 
    aux=float(input("introduce otro numero:"))
    if aux>0:
        cont+=x
        suma2=suma+aux
        if suma2>=x:
            print "Programa terminado"


