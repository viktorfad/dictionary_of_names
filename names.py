import re
import string

with open('names.txt', 'r') as data:
    names = data.read().split(",")

names = [re.sub('"', "", item) for item in names]
names.sort()
sum_all_letters = 0
k = 0
letters_num_sum = {}

for item in names:
    letters_num_sum[item] = 0
    k += 1
    for i in item:
        letters_num_sum[item] += string.ascii_uppercase.index(i) + 1
    sum_all_letters += letters_num_sum[item] * k
print(sum_all_letters)
