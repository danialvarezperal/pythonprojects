#!/usr/bin/python3

#5. Dada una lista de números indicar si está ordenada o no. En caso, de estar desordenada ordenarla.

lista = []
num=int(input("Introduce el primer numero de la lista:"))
while num!=0:
	lista.append(num)
	num=int(input("Introduce el siguiente numero (con 0 finaliza:"))

ordenada=sorted(lista)

if lista == ordenada:
    print(f"La lista {lista} esta ordenada")
else:
    print(f"La lista {lista} NO esta ordenada\nAsi quedaria ordenada {ordenada}")



