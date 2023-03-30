def somaMatriz(matriz):
    if isinstance(matriz, int):
        
        return matriz
    else:
        
        soma = 0
        for elemento in matriz:
            soma += somaMatriz(elemento)
        return soma
    
matriz = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
soma = somaMatriz(matriz)
print(soma) 