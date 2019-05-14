import sympy as sp
import numpy as np

def is_c_prime(x):
    digits = [int(i) for i in str(x)]
    # Checks for any even digits
    if 2 in digits or 4 in digits or 6 in digits or 8 in digits:
        return False 

    for i in range(len(digits) + 1):
        if not sp.isprime(int(''.join(map(str, digits)))):
            return False

        temp = digits[0]
        for j in range(1, len(digits)):
            digits[j - 1] = digits[j]
        digits[len(digits) - 1] = temp
    
    return True

total = 0
for i in range(3, 100, 2):#1000000, 2):
    if is_c_prime(i):
        #print(i, end=',')
        total += 1
print(total)
