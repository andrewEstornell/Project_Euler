import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


# For every N the set {m : phi(m) <= N} has finite cardinality


# Number of test cases
size = 250
# Cardinality of the set {m : phi(m) <= N}
C_N = np.zeros(size - 1)
# Values of N to be tested
Ns = [i for i in range(1, size)]
# Set of all values m s.t. phi(m) <= N, we do not need to recalcuate these values
# if phi(m) <= N then, phi(m) <= N + 1 and so on
ms = {1}
for N in range(1, size):
    # Checks all values up to our analytic upper bound
    for m in range(1, 2 * N ** 2):
        # Skips values of m that have already been calculated
        if m in ms:
            continue
        elif sp.totient(m) <= N:
            ms.add(m)
    C_N[N - 1] += len(ms)

# Stores pairs N and C_N when C_N > 2N (our trent line)
pairs = []
for i in range(len(Ns)):
    if C_N[i] > 2 * Ns[i]:
        pairs.append((Ns[i], C_N[i]))
    # Plots data and lines
plt.figure(figsize=(30, 15))
plt.plot([0, size], [0, size], 'k-')
plt.plot([0, size], [0, 2 * size], 'g-')
plt.plot([0, size], [0, 3 * size], 'k-')
plt.bar(Ns, C_N)
plt.show()
print(C_N, Ns)
print(pairs)


