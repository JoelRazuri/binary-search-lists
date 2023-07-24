"""
    Escribir una función que reciba una lista ordenada y un elemento. Si el elemento se encuentra en la lista, debe encontrar su posición mediante búsqueda binaria y devolverlo. 
    Si no se encuentra, debe agregarlo a la lista en la posición correcta y devolver esa nueva posición. (No utilizar lista.sort().)
"""

lista = [1, 2, 3, 4, 5, 6, 8, 9, 10, 25, 30 ]
num = 50


def busqueda_binaria(lista, elemento):

    izq = 0 
    der = len(lista) - 1 

    while izq <= der:
       
        medio = (izq+der)//2
        
        if lista[medio] == elemento:
            return medio + 1
        elif lista[medio] > elemento:
            der = medio - 1
        else:
            izq = medio + 1

    i = 0
    condicion = True

    while i<len(lista) and condicion:
        if elemento<lista[i]:
            lista.insert(i,elemento)
            condicion = False
        i+=1
    
    if i == len(lista):
        lista.append(elemento)
        i+=1

    

    return i, lista
    


print(busqueda_binaria(lista,num))
    
