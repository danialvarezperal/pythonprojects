''' 10. Pedir el nombre y los apellidos de una persona y mostrar sus
iniciales.'''

val1=str(input("Introduce tu nombre y apellidos: "))
name=val1.split()
inicial= ""
for p in name:
    inicial = inicial + p[0]
    
print("Tus iniciales son :",inicial)









