def selection_sort(list_):
    for i in range(len(list_)):
        min_ = list_[i]
        min_index = i
        for j in range(i, len(list_)):
            if list_[j] < min_:
                min_ = list_[j]
                min_index = j
        temp = list_[i]
        list_[i] = min_
        list_[min_index] = temp
    return list_


file = open('p022_names.txt')

names = []

# Stores names in file
for line in file:
    line_ = line.replace('"', '')
    names_in_line = line_.split(',')
    for name in names_in_line:
        names.append(name)

# Sorts names alphabetically
names = selection_sort(names)

# Totals the names
sum_ = 0
for i in range(len(names)):
    name_value = 0
    for letter in names[i]:
        name_value += ord(letter) - 64
    name_value *= (i + 1)
    sum_ += name_value
print(sum_)


