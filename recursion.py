

# general recursion

# def factorial(n):
#     assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
#     if n in [0, 1]:
#         return 1
#     else:
#         return n * factorial(n - 1)


# print(factorial(-1))


# fibonacci recursion

# def fibonacci(n):
#     assert n >= 0 and int(n) == n, 'Please enter positive number only!'
#     if n in [0, 1]:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# print(fibonacci(-1))

# SUM OF DIGITS recursive case

# def sumOfDigits(n):
#     assert n >= 0 and int(n) == n, 'The number has to be positive!'

#     if n == 0:
#         return 0
#     else:
#         return int(n % 10) + sumOfDigits(n/10)


# print(sumOfDigits(-113))


# Power recursive case

# def power(base, exp):
#     assert exp >= 0 and int(
#         exp) == exp, 'The number has to be positive or whole!'

#     if exp == 0:
#         return 1
#     if exp == 1:
#         return base
#     else:
#         return base * power(base, exp - 1)


# print(power(1, 3))

# Greatest Common Divisor recursive case

def gcd(a, b):
    assert a == 0 and b == 0, 'Bla Bla'

    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(48, 18))
