import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# For every N the set {m : phi(m) <= N} has finite cardinality


#plt.scatter(v2, v1, c=v3)
#plt.show()

# number of m such that phi(m) <= N
size = 150
largest_m = 0

previous_N = 0

ms = np.zeros(size - 1)
Ns = [i for i in range(1, size)]
for N in range(1, size):
    for m in range(1, N**2 + 2):
        if sp.totient(m) <= N:
            ms[N - 1] += 1
    if ms[N - 1] > largest_m:
        print('N = ', N, 'largest m = ', ms[N - 1])
        #print('dN = ', N - previous_N, 'dm = ', ms[N - 1] - largest_m)
        largest_m = ms[N - 1]
        previous_N = N
plt.bar(Ns, ms)
plt.show()
print(ms)

# sqrt(m) <= phi(m)
# m <= phi(m)^2
# sqrt(m) = N <= phi(m)
# m = N**2
# m < N**2 + 1
