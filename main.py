# Practice Question no - 01 n to 1
def n_to_1(n):
    if n == 0:
        return 0
    else:
        print(n)
        return n_to_1(n-1)


# n_to_1(5)

# Practice Question no - 02 -> 1 to n
def one_to_n(n):
    if n == 0:
        return 0
    else:
        one_to_n(n-1)
        print(n)


# one_to_n(5)
# Practice Question no - 02 -> 1 to n

def both(n):
    if n == 0:
        return 0
    else:
        one_to_n(n-1)
        print(n)
        n_to_1(n-1)


# both(5)