import itertools as itr
import sympy as sp

# Takes an indefinitely long list of primes, filters out the first 40 that are prime factors of R(10^9)
print(sum(itr.islice(filter(lambda prime: (pow(10, 10 ** 9, prime * 9) - 1) == 0, sp.sieve), 40)))

