import sympy as sp
import numpy as np


pan_nums = {0}
for i in range(1, 100):
    for j in range(1, 10000):
        digits = str(i) + str(j) + str(i * j)
        if '0' in digits:
            continue
        if len(digits) == 9 and len(set(digits)) == 9:
            pan_nums.add(i*j)

print(np.sum(list(pan_nums)))