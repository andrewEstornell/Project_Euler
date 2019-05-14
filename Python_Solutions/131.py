import sympy as sp
import numpy as np


# How many primes below 1 million has the property that
# n3 + n2p is a perfect cube.

cubes = [i**3 for i in range(1, 10000)]
print('cubes')
counter = 0


for prime in sp.sieve[1: 78499]:
    for n in range(1, 10):
        if n**3 + (n**2 * prime) in cubes:
            counter += 1
            break

print(counter)
