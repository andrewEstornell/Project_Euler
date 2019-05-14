import time
import numpy as np


def is_palindrome(num):
    for i_ in range(len(num)):
        if num[i_] != num[len(num) - 1 - i_]:
            return False
    return True


largest_pal = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        n = i * j
        if n > largest_pal and is_palindrome(str(n)):
            largest_pal = n
print(largest_pal)
