def valor(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        valorMaximo = valor(lista[1:])
        return lista[0] if lista[0] > valorMaximo else valorMaximo

lista = [3, 18, 23, 2, 99, 33]
valorMaximo = valor(lista)
print(valorMaximo) 
