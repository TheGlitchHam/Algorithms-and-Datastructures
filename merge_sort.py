def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Steps:
    1. Divide: Find the midpoint of the list and divide into sublists
    2. Conquer: Recursivly sort the sublists created in previous step
    3. Combine: Merge the sorted sublists created in previous steps

    Takes O(kn log n) time
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    Takes O(k log n) time (k -> the size of the slice)
    """
    mid = len(list)//2


    #TODO Implementierung von split als rekursive methode, wie bei binary search -> Hierdurch kann k eliminiert werden!
    # https://teamtreehouse.com/library/introduction-to-data-structures/the-merge-sort-algorithm/alternate-versions-of-merge-sort
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    Merges two lists, sorting them in the process
    Returns a new merged list

    Runs in overall O(n) time
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1


    while i < len(left):
        l.append(left[i])
        i += 1



    while j < len(right):
        l.append(right[j])
        j += 1

    return l
    


def verify_sorted(list):
    n = len(list)
    if n == 0 or n == 1:
        return True
    return list[0] <= list[1] and verify_sorted(list[1:])


test_list = [4,123,5,6,45,76,345,23,5,543,47,6,4572,57]
sorted_list = merge_sort(test_list)
print(verify_sorted(sorted_list), ": ", sorted_list)