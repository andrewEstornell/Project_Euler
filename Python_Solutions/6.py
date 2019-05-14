import numpy as np

sum_of_squares = 0
for i in range(1, 101):
    sum_of_squares += i**2
difference = np.sum([i for i in range(1, 101)])**2 - sum_of_squares
print(difference)