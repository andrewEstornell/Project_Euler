import sympy as sp
import numpy as np

# Pandigital prime, a prime that makes use of the digits 1 to n exactly
# Find the largest n-digit pandigital prime.

largest_prime = 0
for i in range(3, 10):
    digits = [j for j in range(1, i + 1)]

    for k in range(int(sp.factorial(len(digits)))):
        temp = digits[k % (len(digits) - 1)]
        digits[k % (len(digits) - 1)] = digits[(k % (len(digits) - 1)) + 1]
        digits[(k % (len(digits) - 1)) + 1] = temp

        num = sum([digits[i] * (10**i) for i in range(len(digits))])
        if sp.isprime(num):
            if num > largest_prime:
                print(num)
                largest_prime = num
