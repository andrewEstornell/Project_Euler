import sympy as sp
import numpy as np
import matplotlib.pyplot as plt




def is_fact_sum(x):
    digits = str(x)
    return x == np.sum([facts[int(i)] for i in digits])

def fact_sum(x):
    digits = str(x)
    return np.sum([facts[int(i)] for i in digits])


facts = [np.math.factorial(i) for i in range(10)]

dig_fact = []
total = 0
for i in range(3, 2500000):
    #dig_fact.append(fact_sum(i))
    if is_fact_sum(i):
        total += i
print(total)

#plt.plot(dig_fact)
#plt.plot([i for i in range(3, 2500000)])
#plt.show()