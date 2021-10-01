

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

x
