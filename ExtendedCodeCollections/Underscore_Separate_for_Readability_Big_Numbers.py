# Underscore_Separate_for_Readability_Big_Numbers.py
#
# author: kaoru
# date: 29.09.23

# Python allows to use underscore as a easy to read mark.

num_1 = 10_000_000  # cannot use , as 10,000,000
num_2 = 100_000_000_000

total = num_1 + num_2
print(total)

# to make it easy to read output, use string format
print(f'{total:,}')