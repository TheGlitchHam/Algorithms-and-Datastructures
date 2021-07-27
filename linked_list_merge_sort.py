from linked_list import LinkedList


def merge_sort(linked_list):
    """
    Sorts linked list in ascending order
    - Recursively divides linked list into sublists containing a single node
    - Repeatedly merge the sublists to produce sorted sublists until one remains

    Returns a sorted linked list

    Runs in O(kn log n)
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    """
    Runs in O(k log n) time
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2
        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    """
    Runs in O(n) time
    """
    merged = LinkedList()
    # fake head for convenience
    merged.add(0)
    current = merged.head

    left_head = left.head
    right_head = right.head
    while left_head or right_head:
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            if left_head.data < right_head.data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        current = current.next_node

    # remove fake head
    merged.head = merged.head.next_node
    return merged


def verify_sorted(linked_list):
    current_node = linked_list.head
    while current_node and current_node.next_node:
        if current_node.data > current_node.next_node.data:
            return False
        else:
            current_node = current_node.next_node
    return True


l = LinkedList()
l.add(2)
l.add(43)
l.add(2)
l.add(34)
l.add(13)
l.add(5)
l.add(67)
l.add(56)
l.add(326)
print(verify_sorted(l))
sorted_linked_list = merge_sort(l)
print(verify_sorted(sorted_linked_list))
