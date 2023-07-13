#!/usr/bin/python3

#1. Realizar un programa que pida por teclado una cantidad que representa los segundos, e  indicará cuantos minutos son y cuantas horas correspondientes.

def numSeg(varCant):
	# Primera parte haciendo division evitando el resto
	varMin= varCant // 60
	varHora= varCant // 60 // 60
	
	# Segunda parte haciendo division cogiendo el resto o residuo
	minRest= varMin % 60
	segRest= varCant % 60

	print("\nDaria los siguientes parametro:\n")
	print("Segundos "+str(segRest)+" Minutos "+str(minRest)+" Horas "+str(varHora))


varCant=int(input("Introduce un numero de segundos: "))

numSeg(varCant)







