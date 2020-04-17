# COMMENT 0 1 1 2 3 5 8 13
n = 5
# Initialise
term_1 = 0
term_2 = 1

for i in range(n):
    # Create next value in sequence
    result = term_1 + term_2

    # Print seq output
    print(term_1)

    # Updating of our generator terms
    term_1 = term_2
    term_2 = result
    