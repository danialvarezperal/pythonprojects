''' 8. Calcular la distancia entre un punto final y un punto inicial entre dos valores introducidos 
por teclado. (Siempre el resultado debe ser positivo).'''

prin=float(input("Intoduce el punto inicial: "))

ult=float(input("Introduce el punto final: "))

result=prin-ult

if result<0:
    result=result*-1
    print("Esta es la distancia entre el punto final y el punto inicial: ",result)
else:
    print("Este esla distancia entre el punto final y el punto inicial: ",result)




