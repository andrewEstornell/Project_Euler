import numpy as np
import sympy as sp


# Pentagonal number => p_n = n(3n - 1) / 2.
# First 10 are 1, 5, 12, 22, 25, 51, 70, 92
# Find P_j and P_k such that p_j + p_k is pentagonal and p_j - p_k is pentagonal
# and D = |p_k - p_j| is minimized, what is D

# 3n^2 - n  - 2p = 0
# (-b +- sqrt(b^ 2 - 4ac)) / 2a

def pent(n):
    return (n * (3 * n - 1)) // 2


def is_pent(x):
    r = np.sqrt(1 + 4 * 3 * 2 * x)
    if r.is_integer():
        if r % 6 == 1:
            return True
        elif r % 6 == 5:
            return True
    return False


min_D = 1000
for i in range(1, 1000):
    for j in range(1, 1000):
        if i == j:
            continue
        p_i = pent(i)
        p_j = pent(j)
        if not is_pent(p_i + p_j):
            continue
        if not is_pent(np.abs(p_i - p_j)):
            continue
        if np.abs(p_i - p_j) < min_D:
            min_D = np.abs(p_i - p_j)
            print(min_D)