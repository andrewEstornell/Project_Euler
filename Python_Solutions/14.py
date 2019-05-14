
previous_values = {1, 2}
largest_value = 0
max_length = 0

for i in range(1, 1000000):
    length = 1
    starting_value = i
    while i != 1:
        if i % 2 == 0:
            i = int(i / 2)
        else:
            i = 3*i + 1
        length += 1
    if length > max_length:
        largest_value = starting_value
        max_length = length

print(max_length)
print(largest_value)
