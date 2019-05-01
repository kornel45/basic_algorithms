import os

import numpy as np


def gen_one_file(n, k):
    if not os.path.exists('data'):
        os.mkdir('data')
    file_name = f'data/{n}_{k}_3SUM_ROWS.txt'
    random_integer_matrix = np.random.randint(-k, k + 1, (1, n))
    np.savetxt(file_name, random_integer_matrix, fmt='%d')


if __name__ == '__main__':
    k = 10 ** 6
    sizes = [50, 100, 250, 500, 1000, 2000, 4000, 8000, 16000]
    for f in os.listdir('data'):
        os.remove(f'data/{f}')
    for n in sizes:
        gen_one_file(n, n ** 2)
