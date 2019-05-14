import numpy as np
import sympy as sp


# Find the sum of all numbers that can be written as the sum of the 5th power of their digits

# upper bound for a number n digits long n9^5
# Since 7*9^5 == 413343, having only 6 digits, we need only check numbers up to 9,999,999


def fth_sum_of_digits(n):
    str_n = str(n)
    sum_ = 0
    for digit in str_n:
        sum_ += int(digit) ** 5
    return sum_


total = 0
for i in range(2, 9999999):
    if i == fth_sum_of_digits(i):
        total += i
print(total)