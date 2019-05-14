# Smallest x, s.t. x, 2x, 3x, 4x, 5x, 6x have the same digits


def same_digits(a, b):
    return [list(str(a)).count(str(i)) for i in range(10)] == [list(str(b)).count(str(i)) for i in range(10)]


x = 1
while True:
    if same_digits(x, 2*x) and same_digits(x, 3*x) and same_digits(x, 4*x) and same_digits(x, 5*x) and same_digits(x, 6*x):
        print(x)
        break
    x += 1