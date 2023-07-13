#!/usr/bin/python3

#4. Utilizando la lista del ejercicio anterior, pedir por teclado una cadena e indiciar si esta cadena se encuentra en la lista.

lista=["la","ruta","nos","aportó","otro","paso","natural"]

palabra=input("Introduce una palabra:")

#Control para que consulta la palabra con cada elemento de la lista
if palabra in lista:
    print(f"La cadena ({palabra}) se encuentra en la lista")
else:
     print(f"La cadena ({palabra}) no esta en la lista")

