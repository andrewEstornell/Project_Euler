import numpy as np
import sympy as sp


# Goladbach's other conjecture
# Every odd composite number can be written as the sum of a prime and twice a square
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square
# o != p + 2 * s^2 for any p and any s.

def conj(odd):
    # Finds if 'odd' can be wirtten as the sum of a prime and twice a square
    for p in sp.sieve[1:odd - 2]:
        for s in range(1, odd):
            if odd == p + (2 * (s ** 2)):
                return True
            if 2 * s ** 2 > (odd - p - 1):
                break

    return False


for i in range(5, 10000, 2):
    if not sp.isprime(i):
        if not conj(i):
            print(i)
