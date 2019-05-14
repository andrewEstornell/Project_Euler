import numpy as np


def calc_val(word, alphabet):
    val = 0
    for c in word:
        val += alphabet.index(c) + 1
    return val


file = open("p042_words.txt", "r")
words = file.readline().replace("\"", '').split(",")
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
trig_nums = [0.5*i*(i + 1) for i in range(1, 1000)]
num_words = 0
for word in words:
    if calc_val(word, alphabet) in trig_nums:
        num_words += 1
print(num_words)







