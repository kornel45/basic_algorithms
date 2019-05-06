import os
import time
from multiprocessing.pool import Pool

from gen_data import read_one_file


def naive_solution(array, n):
    """ O( n^3 ) """
    count = 0
    result = []
    s = time.time()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if k != j + 1 and array[k] == array[k - 1]:
                    continue
                if array[i] + array[j] + array[k] == 0:
                    count += 1
                    result.append([array[i], array[j], array[k]])
    e = time.time()
    print(f'Naive solution for {n} took: {e - s} seconds and found {count} sums')
    return result


def hash_solution(array, n):
    """ O( n^2 ) """
    result = []
    count = 0
    s = time.time()
    for i in range(n):
        if i != 0 and array[i] == array[i - 1]:
            continue
        seen_set = set()
        j = i + 1
        while j + 1 < n:
            if -(array[i] + array[j]) in seen_set:
                count += 1
                result.append([array[i], array[j], -(array[i] + array[j])])
                while array[j + 1] == array[j] and j + 1 < n:
                    j += 1
            seen_set.add(array[j])
            j += 1
    e = time.time()
    print(f'Hash solution for {n} took: {e - s} seconds and found {count} sums')
    return count


def sort_solution(array, n):
    """ O( n^2 ), array values must be unique """
    count = 0
    result = []
    s = time.time()
    array.sort()
    for i in range(n - 1):
        a = array[i]
        start = i + 1
        end = n - 1
        while start < end:
            b = array[start]
            c = array[end]
            if a + b + c == 0:
                count += 1
                result.append([a, b, c])
                start = start + 1
                end = end - 1
            elif a + b + c > 0:
                end -= 1
            else:
                start += 1
    e = time.time()
    print(f'Sort solution for {n} took: {e - s} seconds and found {count} sums')
    return count


if __name__ == '__main__':
    array_list = []
    array_names = []
    for f_path in sorted(os.listdir('data'), key=lambda x: int(x.split('_')[0])):
        data = read_one_file(f_path)
        array_list.append(data)
        array_names.append(len(data))

    with Pool(6) as pool:
        pool.starmap(sort_solution, (x for x in zip(array_list, array_names)))
