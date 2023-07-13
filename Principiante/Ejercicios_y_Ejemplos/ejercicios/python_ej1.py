#!/usr/bin/python3

#1. Almacenar en una lista los números pedidos por teclado hasta que se introduzca un número negativo. Mostrar la lista de partida y calcular el número máximo

#Declaramos la lista vacia
lista = []
#Pedimos el numero que sera previo al bucle while por si es un numero negativo
num=int(input("Introduce un numero:"))
#Bucle while por si es un numero negativo
while num>=0:
#agregamos el numero a la lista
	lista.append(num)
	#volvemos a pedir el numero pero ahora dentro del bucle
	num=int(input("Introduce un numero:"))

#Bucle for mostrara todos los numeros introducidos en la lista
for num in lista:
	print(num)
