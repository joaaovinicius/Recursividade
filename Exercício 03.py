def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)
numero1 = 50
numero2 = 29
print("O MDC de", numero1, "e", numero2, "é:", mdc(numero1, numero2))
