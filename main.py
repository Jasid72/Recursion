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

# Practice Question no - 03 Factorial
def factorial(n):
    assert int(n) >= 0, "Input must be Positive"
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(f"Factorial of {10} is :", factorial(10))

# Practice Question no - 04 Sum
def Sum(n):
    assert int(n) >= 0, "Input must be Positive"
    if n == 0:
        return 0
    else:
        return n + Sum(n-1)


print(f"Sum of {5} is :", Sum(5))


# Practice Question no - 05 Sum of Digits
def Sum_Of_Digits(n):
    assert int(n) >= 0, "Input must be Positive"
    if n == 0:
        return 0

    return int(n % 10 + Sum_Of_Digits(n//10))


print(f"Sum of Digits {1342} is :", Sum_Of_Digits(1342))

# Practice Question no - 06 Product of digits
def Product_Of_Digits(n):
    assert int(n) >= 0, "Input must be Positive"
    if n%10 == n:
        return n

    return int(n % 10 * Product_Of_Digits(n//10))


print(f"Product of {55} is :", Product_Of_Digits(55))


# Practice Question no - 07 Reverse Number
