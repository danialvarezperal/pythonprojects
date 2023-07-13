#!/usr/bin/python3

#3. Dada la lista [‘la"’","’"ruta"’","’"nos"’","’"aportó"’","’"otro"’","’"paso"’","’"natural"’"] crear un programa que cree una nueva lista, pero invertida a la original. El programa debe mostrar ambas listas.

def listaReversa():
    lista=["la","ruta","nos","aportó","otro","paso","natural"]
    #Con ::-1 para poner la lista de palabras al reves
    listaReversa=lista[::-1]


    print(f"Lista original: {lista} \nLista invertida: {listaReversa}")

listaReversa()


