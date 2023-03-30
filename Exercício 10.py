def contador(lista, elemento):
    if not lista:
        return 0
    elif lista[0] == elemento:
        return 1 + contador(lista[1:], elemento)
    else:
        return contador(lista[1:], elemento)
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
elemento = 1
ocorrencias = contador(lista, elemento)
print(ocorrencias) 