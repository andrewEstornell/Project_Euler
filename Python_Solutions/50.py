import sympy as sp
import numpy as np

one_mill = 1000000
primes = sp.sieve[1:78497]


longest = [0 for i in range(3)]

max_index = len(primes)
for i in range(max_index):
    j = i
    consec_sum = 0
    while consec_sum < one_mill and j < max_index:
        consec_sum += primes[j]
        # Checks if current length greater than max length
        if j - i > longest[0]:
            # Checks if consec_sum is prime
            if consec_sum in primes:
                longest[0] = j - i
                longest[1] = i
                longest[2] = consec_sum
        j += 1
print(longest[2])
