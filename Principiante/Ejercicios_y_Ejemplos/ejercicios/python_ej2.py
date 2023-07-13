#!/usr/bin/python3

#2. Realizar un programa que pida por teclado una palabra y compruebe si es palíndromo (se leen igual hacia ambos lados. Ejemplo: oro, radar, rallar.

word=input("Introduce una palabra : ")

#Control de la lista si es palindromo con la funcion ::-1 para poner la palabra al reves y la compare
if word == word [::-1]:
    print(f"La palabra {word} es un palindromo.")
else :
    print(f"La palabra {word} NO es un palindromo.")
