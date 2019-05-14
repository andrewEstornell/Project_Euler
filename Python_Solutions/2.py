def fib(sequence, limit):
    fn = sequence[len(sequence) - 1] + sequence[len(sequence) - 2]
    if fn > limit:
        return sequence
    else:
        sequence.append(fn)
        return fib(sequence, limit)


def make_list(list_, n):
    if n > 5:
        return list_
    else:
        list_.append(10)


sum_ = 0
for i in fib([1, 1], 4000000):
    if i % 2 == 0:
        sum_ += i
print(sum_)
