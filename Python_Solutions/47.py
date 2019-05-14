import sympy as sp
import itertools as itr

# Find the first four consecutive integers to have four distinct prime factors each.
#  What is the first of these numbers?

lam_j = lambda j: len(sp.primefactors(j)) == 4 and len(sp.primefactors(j + 1)) == 4 and \
                  len(sp.primefactors(j + 2)) == 4 and len(sp.primefactors(j + 3)) == 4
print(sum(itr.islice(filter(lam_j, itr.count()), 1)))

