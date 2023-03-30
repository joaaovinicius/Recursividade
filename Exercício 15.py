def mediana(lista):
    n = len(lista)
    if n == 0:
        return None
    elif n % 2 == 1:

        return sorted(lista)[n//2]
    else:
       
        sorted_numbers = sorted(lista)
        esquerda = (n - 1) // 2
        direita = n // 2
        return (sorted_numbers[esquerda] + sorted_numbers[direita]) / 2

lista = [3,  4,  10, 9, 21, 68, 15, 25]
media = mediana(lista)
print(media)
