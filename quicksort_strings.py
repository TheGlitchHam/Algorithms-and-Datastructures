import sys
import time
from load import load_string

unsorted_names = load_string(sys.argv[1])


def quicksort(list):
    if len(list) <= 1:
        return list
    less_than_pivot = []
    greater_than_pivot = []
    pivot = list[0]
    for entry in list[1:]:
        if entry <= pivot:
            less_than_pivot.append(entry)
        else:
            greater_than_pivot.append(entry)
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


start = time.time()
sorted_names = quicksort(unsorted_names)
end = time.time()
print(sorted_names)
print("Time: " + str(end - start) + "s")
