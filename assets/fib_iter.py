# Iterative approach to fib sequence

def fib(n):
    a,b = 0,1
    for i in range(n):
        a,b = b, a+b
    return a

for i in range(15):
    print(fib(i))