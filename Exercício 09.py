def m(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return (lista[0] + m(lista[1:])*len(lista[1:]))/(len(lista))
        
lista = [3,  4,  5, 9, 2, 6, 5, 10]
media = m(lista)
print(media)
