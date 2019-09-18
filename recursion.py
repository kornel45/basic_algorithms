# /usr/bin/python
"""This file contains few simple algorithms that use recursion"""


def euclidean_algorithm(a, b):
    """Finds the biggest common divisor"""
    if a == 0: return b
    if b == 0: return a
    r = a % b
    return euclidean_algorithm(b, r)


def recurrent_sum_of_elements_in_list(lst):
    """Calculates in recurrent way sum of all elements in lst"""
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    return lst[0] + recurrent_sum_of_elements_in_list(lst[1:])


def recurrent_max_value_in_list(lst, max_value):
    """Calculates in recurrent way maximum value in a list"""
    if len(lst) == 0:
        return max_value
    elif lst[0] > max_value:
        max_value = lst[0]
    return recurrent_max_value_in_list(lst[1:], max_value)


def sum_without_dummy_variable(lst):
    if len(lst) > 0:
        max_value = lst[1]
        return recurrent_max_value_in_list(lst, max_value)
    return 0


def recurrent_binary_search(lst, value):
    low = 0
    high = len(lst)
    mid = int((high + low) / 2)
    if lst[mid] == value:
        return mid
    elif lst[mid] < value:
        return recurrent_binary_search(lst[mid:], value)
    elif lst[mid] > value:
        return recurrent_max_value_in_list(lst[:mid], max_value)
    return None


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    result_gcd = euclidean_algorithm(168, 64)
    assert result_gcd == 8

    result_sum = recurrent_sum_of_elements_in_list(lst)
    assert result_sum == 15
    assert 5 == recurrent_max_value_in_list(lst[::-1], lst[0])
    assert 5 == recurrent_max_value_in_list(lst, lst[0])
    assert 5 == recurrent_max_value_in_list([1, 2, 5, 3, 4], lst[0])
    assert 5 == recurrent_binary_search(range(10), 5)
