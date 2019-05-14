import numpy as np
import scipy as sp


vals = []
for i in range(10, 100):
    for j in range(10, 100):
        if i >= j:
            continue
        i_dig = str(i)
        j_dig = str(j)
        if i_dig[1] == '0' and j_dig[1] == '0':
            continue
        if i_dig[0] == j_dig[1] and j_dig[0] != '0':
            if int(i_dig[1])/int(j_dig[0]) == int(i)/int(j):
                vals.append([i, j])
        if i_dig[1] == j_dig[0] and j_dig[1] != '0':
            if int(i_dig[0])/int(j_dig[1]) == int(i)/int(j):
                vals.append([i, j])

nume = np.product(np.asarray(vals)[:, 0])
deno = np.product(np.asarray(vals)[:, 1])


g = sp.gcd(nume, deno)

print(deno / g)




