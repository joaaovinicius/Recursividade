result = 1
def Potencia(base, expoente):
    global result
    if expoente == 0:
        return result
    else:
        result = result * base
        return Potencia(base, expoente-1)


base = 2
potencia = 10
print(Potencia(base,potencia))