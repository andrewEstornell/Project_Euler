import sympy as sp
import numpy as np

# how many ways can 200 be made using any number of 1s, 2s, 5s, 10s, 20s, 50s, and 100s

target = 200
total_ways = 0
for i1 in range(target + 1):
    for i2 in range(0, target + 1, 2):
        if i1 + i2 > 200:
            break
        for i5 in range(0, target + 1, 5):
            if i1 + i2 + i5 > 200:
                break
            for i10 in range(0, target + 1, 10):
                if i1 + i2 + i5 + i10 > 200:
                    break
                for i20 in range(0, target + 1, 20):
                    if i1 + i2 + i5 + i10 + i20 > 200:
                        break
                    for i50 in range(0, target + 1, 50):
                        if i1 + i2 + i5 + i10 + i20 + i50 > 200:
                            break
                        for i100 in range(0, target + 1, 100):
                            if i1 + i2 + i5 + i10 + i20 + i50 + i100 > 200:
                                break
                            elif i1 + i2 + i5 + i10 + i20 + i50 + i100 == target:
                                total_ways += 1
print(total_ways + 1)