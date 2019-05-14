import sympy as sp
import numpy as np
print(np.sum([i for i in range(2000000) if sp.isprime(i)]))
