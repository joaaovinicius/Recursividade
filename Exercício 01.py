def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

result = fatorial(5)
print(result)