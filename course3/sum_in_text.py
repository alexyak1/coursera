import re

file = open("regex_sum_891946.txt", "r") 
text = file.read().split(',')

all_numbers = []
for one_line in text:
    numbers = re.findall('[0-9]+', one_line)

    sum_in_line = 0
    for number in numbers:
        sum_in_line = sum_in_line + int(number)

    all_numbers.append(sum_in_line)

print(sum(all_numbers))