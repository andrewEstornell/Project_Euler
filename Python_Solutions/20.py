import sympy as sp

fact = str(sp.factorial(100))
sum_ = 0
for digit in fact:
    sum_ += int(digit)
print(sum_)
