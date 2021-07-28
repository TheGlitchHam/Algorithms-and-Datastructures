import random
import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])


def is_sorted(list):
    for index in range(len(list) - 1):
        if list[index] > list[index + 1]:
            return False
    return True


def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        print(attempts)
        random.shuffle(values)
        attempts += 1
    return values


print(bogo_sort(numbers))
