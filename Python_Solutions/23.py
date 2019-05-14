import sympy as sp
import numpy as np

upper_bound = 28123

smallest_abundant = 12


def is_abundant(x):
    fact1 = []
    for i in range(1, int(np.floor(np.sqrt(x)))):
        if x % i == 0:
            fact1.append(i)
    factors2 = [x // i for i in fact1]
    if np.sum(fact1) + np.sum(factors2) > x:
        return True 

class Square:
    
    def __init__(self):
        self.a = 3
        self.b = 4
        self.c = 5
    
    def calc_area(self):
        return self.a * self.b / 2



#def is_bundant_sum(x):


