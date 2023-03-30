def soma(n):
    if n < 10:
        return n
    else:
        ultimo = n % 10
        resto = n // 10
        return ultimo + soma(resto)
n = 123456789
soma = soma(n)
print("A soma dos dígitos de", n, "é", soma)
