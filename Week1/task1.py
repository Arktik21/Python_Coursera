import sys

input_numbers = sys.argv[1]
sum_of_numbers = 0

for digit in input_numbers:
    sum_of_numbers += int(digit)

print(sum_of_numbers)