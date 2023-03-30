def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def printFibonacci(n):
    for i in range(n):
        print(fib(i))

printFibonacci(10)
