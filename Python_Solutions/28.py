import numpy as np

# Stores our numbers, there will be 1001^2 number of them
numbers = np.zeros(1001*1001)
for i in range(1001*1001):
    numbers[i] = i + 1

# Extracts the diagonal numbers and sums them
sum_ = 0
scalar = 2
i = 0
j = 0
while i <= len(numbers):
    sum_ += numbers[i]
    i += scalar
    if j == 3:
        scalar += 2
        j = 0
    else:
        j += 1
print(int(sum_))
