
# Stores the generated digits
decimal_string = ''
# next digit to add
i = 1
# Counts the number of digits that have been added
digits = 0

# adds the first 100000 digits to the number
while digits <= 1000000:
    decimal_string += str(i)
    digits += len(str(i))
    i += 1

product = 1
# Gets the product at each power of 10 index
for i in range(7):
    product *= int(decimal_string[10**i - 1])
print(product)
