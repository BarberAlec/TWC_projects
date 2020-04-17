
def isPrime(x):
    # Takes in number x and returns true if it is a prime and false if not a prime.

    # Speacial case: 0
    if x==0:
        return False

    for i in range(2,x):
        if x%i == 0:
            return False
    return True


for i in range(20):
    print(isPrime(i))


[print(f"isPrime {i}: {isPrime(i)}") for i in range(20)]