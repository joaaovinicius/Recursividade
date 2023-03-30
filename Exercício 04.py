def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

def mmc(a, b):
  
    return (a * b) // mdc(a, b)

def r(a, b):
    
    return mmc(a, b)

a = 60
b = 24
MMC = r(a, b)
print(f"O MMC entre {a} e {b} é {MMC}.")