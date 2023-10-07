SampleList = []


def multi_all(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multi_all(8, 2, 3, -1, 7))
