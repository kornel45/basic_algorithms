#!/usr/bin/python
import random


def quick_sort(lst):
    """Quick sort algorithm implementation"""
    if len(lst) < 2:
        return lst
    pivot = lst[random.randint(0, len(lst)-1)]
    left_list = []
    right_list = []
    for val in lst:
        if val < pivot:
            left_list.append(val)
        elif val > pivot:
            right_list.append(val)
    return quick_sort(left_list) + [pivot] + quick_sort(right_list)

if __name__ == '__main__':
    ar = [1, 5, 2, 0, 3, 7]
    assert sorted(ar) == quick_sort(ar)
