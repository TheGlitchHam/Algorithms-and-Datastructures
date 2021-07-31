import sys
from load import load_numbers
import time
"""
Quicksort algorithm:
Pick a pivot (random value from list)
Split the list into two sublists, one with values smaller or equal,
one with values greater than pivot
Through recursion, this happens with every sublist, too
In the end, we simply return the two sublists with their recursive calls, and
merge it with the pivot at the middle 
Steps:
1. Pick pivot
2. Split into two sublists, [] <= pivot < []
3. Recursive quicksort on both sublists
4. Return quicksorted lists and merge them with pivot in the middle

Runtime: O(n²) at worst, O(n log n)
However, quicksort often performs at best case speed
"""


numbers = load_numbers(sys.argv[1])


def quicksort(values):
    if len(values) <= 1:
        return values

    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    # print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


start = time.time()
result = (quicksort(numbers))
end = time.time()
print(result)
print("Time: ", (end - start))
