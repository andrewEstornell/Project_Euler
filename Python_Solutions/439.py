import numpy as np


def S(N):
    return sum([sum([d(i * j) for j in range(1, N + 1)]) for i in range(1, N + 1)])


def d(k):
    return sum([i for i in range(1, k+1) if k % i == 0])


print(S(10**2))
