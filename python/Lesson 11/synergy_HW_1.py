import math

def calculate_factorial(n):
    return math.factorial(n)

def factorial_list(n):
    result = []
    factorial_n = calculate_factorial(n)
    for i in range(1, factorial_n + 1) :
        result.append(calculate_factorial(i))
    result.reverse()
    return result

print(factorial_list(3))