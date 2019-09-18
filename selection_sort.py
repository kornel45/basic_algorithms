#!/usr/bin/python
def find_smallest_value(lst):
    """Finds smallest value in list and returns its index"""
    smallest_value = lst[0]
    smallest_index = 0
    for i, val in enumerate(lst):
        if val < smallest_value:
            smallest_value = val
            smallest_index = i
    return smallest_index


def selection_sort(lst):
    """Sorts lst with selection sort from smallest to biggest"""
    result_lst = []
    for _ in range(len(lst)):
        smallest_value = lst.pop(find_smallest_value(lst))
        result_lst.append(smallest_value)
    return result_lst


if __name__ == '__main__':
    import random

    random_lst = [random.random() for _ in range(5)]
    sorted_lst = selection_sort(random_lst)
    print(sorted_lst)
