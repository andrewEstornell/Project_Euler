import numpy as np
import sympy as sp


def is_trunc_prime(p):
    p_str = str(p)
    for i in range(len(p_str)):
        if not sp.isprime(int(p_str[:len(p_str) - i])):
            return False
        if not sp.isprime(int(p_str[i:])):
            return False
    return True


primes = []
i = 10
while True:
    i += 1
    if is_trunc_prime(i):
        primes.append(i)
    if len(primes) == 11:
        break
print(sum(primes))
