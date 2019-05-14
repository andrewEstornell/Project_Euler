import numpy as np
import sympy as sp

num_primes = 0
best_ab = (0, 0)

for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        i = 0
        while sp.isprime((i ** 2) + (a * i) + b):
            i += 1
        if i > num_primes:
            num_primes = i
            best_ab = (a, b)
print(best_ab[0] * best_ab[1])
