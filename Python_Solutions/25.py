f_1 = 1
f_2 = 1
i = 2
while len(str(f_2)) < 1000:
    t = f_2
    f_2 = t + f_1
    f_1 = t
    i += 1
print(i)
