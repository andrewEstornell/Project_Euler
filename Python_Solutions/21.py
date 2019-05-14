import sympy as sp
import numpy as np


# d(a) = d_1 + d_2 + ... + d_n where d_1, ..., d_n are all proper divisors of a
# Amicable := d(a) == d(b) with a != b
# Find the sum of all amicable numbers less than 10,000


def di(a):
    return sum([i for i in range(1, int(a / 2) + 1) if a % i == 0])


amicable_nums = {0}
for n in range(1, 10000):
    d = di(n)
    if d != n and di(d) == n:
        amicable_nums.add(n)
print(sum(amicable_nums))

