import sympy as sp
import numpy as np


# Starting with 69 produces a chain of five non-repeating terms,
# but the longest non-repeating chain with a starting number below one million is sixty terms.
# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms

def f(x):
    digits = str(x)
    sum_ = 0
    for digit in digits:
        sum_ += sp.factorial(int(digit))
    return sum_


# Stores the length of the cycle and the starting value of the cycle
cycles = {1: 1}
non_repeat_6s = []


for n in range(2, 1000000):
    x_n = f(n)
    length_n = 1
    cycle_n = [n]
    while True:
        if x_n in cycles:
            if length_n + cycles[x_n] == 6:
                non_repeat_6s = n
            cycles[n] = length_n + cycles[x_n]
            break
        if x_n in cycle_n:
            cycles[n] = length_n
            break
        else:
            cycle_n.append(x_n)
        x_n = f(x_n)
        length_n += 1

print(len([value for value in cycles.values() if value == 60]))
