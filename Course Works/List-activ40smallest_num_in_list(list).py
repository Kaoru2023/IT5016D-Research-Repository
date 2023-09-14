# List-activ40smallest_num_in_list(list).py
#
# author: Kaoru
# date: 17.08.23

list_2 = [1, 19, 4, 8]


# fetching smallest number in list
def smallest_num_in_list(list):
    min = list[0]
    for a in list:
        if a < min:
            min = a
    return min


print(smallest_num_in_list(list_2))


# fetching largest number in list
def largest_num_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max


print(largest_num_in_list(list_2))
