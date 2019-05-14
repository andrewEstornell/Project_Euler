import sympy as sp

for i in range(100000):
    tri_number = 0
    for j in range(i + 1):
        tri_number += j
    num_divisors = 1
    for j in range(2, int(sp.sqrt(tri_number)) + 1):
        if tri_number % j == 0:
            num_divisors += 1
        if num_divisors > 250:
            print(tri_number)
            exit(0)
