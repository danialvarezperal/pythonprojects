#!/usr/bin/python3

#6. Realizar un programa que pida por teclado una palabra y una vocal e indique el número de veces que aparece dicha vocal.

text=input("Ingrese una palabra y una vocal separa por espacio:")
#Seleccionamos la palabra que nos hace falta para cada caso 
word=text.split()[0]
vocal=text.split()[1]
veces=0
i=0
#Un bucle que segun la longitud de la palabra sumara al contador o se saldra
while i < len(word):
    if word[i] == vocal:
        veces= veces+1
    i=i+1

print(f"La palabra {word} tiene {veces} veces la vocal {vocal}")