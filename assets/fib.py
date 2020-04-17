# COMMENT: 0 1 1 2 3 5 8 13
n = 7

a = 0
b = 1

for i in range(n):
    # Get next value
    next_term = a + b

    # Print value
    print(a)

    # Update previous terms/generator terms
    a = b
    b = next_term
    
