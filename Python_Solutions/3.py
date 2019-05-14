import numpy as np


def is_prime(p):
    for d_ in range(3, int(np.sqrt(p))):
        if p % d_ == 0:
            return False
    return True


n = 600851475143
largest_prime = -1
for d in range(2, int(np.sqrt(n))):
    if n % d == 0 and is_prime(d):
        largest_prime = d
print(largest_prime)
