# 0 1 1 2 3 5 8 13
n = 5


first_val = 0
second_val = 1

for i in range(n):
    print(first_val)
    result = first_val + second_val

    first_val = second_val
    second_val = result

    