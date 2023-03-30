def valorminimo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        resto = valorminimo(lista[1:])
    
        if lista[0] < resto:
            return lista[0]
        else:
            return resto

lista = [15, 11, 14, 31, 7, 55, 9, 27]
print(valorminimo(lista))
