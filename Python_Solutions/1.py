import time
start = time.clock()
sum_ = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum_ += i
print("time = ", start-time.clock(), "Solution = ", sum_)
