import random


def merge_sort(list, lower_bound, upper_bound):
    """
    Implementation of merge sort algorithm with iteration
    Will run in O(n log n), as list is not divided using split, but rather with upper and lower
    index usage, eliminating the O(k log n) time with splitting

        Steps:
        1. Divide: Find the midpoint of the list and divide into sublists
        2. Conquer: Recursivly sort the sublists created in previous step
        3. Combine: Merge the sorted sublists created in previous steps

    """
    if upper_bound - lower_bound >= 2:
        mid = (lower_bound + upper_bound)//2
        merge_sort(list, lower_bound, mid)
        merge_sort(list, mid, upper_bound)
        merge(list, lower_bound, mid, upper_bound)
    return list


def merge(list, left, mid, right):
    len_left = calc_length(left, mid)
    len_right = calc_length(mid, right)
    tmp_list = [0] * (len_left + len_right)
    lower_index, upper_index, tmp_index = left, mid, 0

    while lower_index < mid and upper_index < right:
        if list[lower_index] <= list[upper_index]:
            tmp_list[tmp_index] = list[lower_index]
            lower_index += 1
        else:
            tmp_list[tmp_index] = list[upper_index]
            upper_index += 1
        tmp_index += 1

    if lower_index == mid:
        tmp_list[tmp_index:] = list[upper_index:right]
    else:
        tmp_list[tmp_index:] = list[lower_index: mid]

    list[left:right] = tmp_list
    return list


def calc_length(lower_index, upper_index):
    return upper_index-lower_index


def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True
    return list[0] <= list[1] and verify_sorted(list[1:])


test_list = random.sample(range(0, 100), 50)
print(test_list)
sorted_list = merge_sort(test_list, 0, len(test_list))
print(verify_sorted(sorted_list), ": ", sorted_list)
