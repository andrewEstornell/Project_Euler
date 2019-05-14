import sympy as sp

for a in range(1000):
    for b in range(1000):
        if a**2 + b**2 == (1000 - a - b)**2:
            print(a*b*sp.sqrt(a**2 + b**2))
            break
