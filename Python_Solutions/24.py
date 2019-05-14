import itertools as itr
import numpy as np


print(sorted(map(lambda x: np.sum([x[i]*10**(9-i) for i in range(10)]), itr.permutations([i for i in range(10)], 10)))[999999])
