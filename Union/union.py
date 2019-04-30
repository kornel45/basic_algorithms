import time
from multiprocessing import Pool

import numpy as np


class QuickFind:
    def __init__(self, n):
        self.union_array = list(range(n))

    def union(self, p, q):
        if not self.is_connected(p, q):
            tmp = self.union_array[q]
            for i, value in enumerate(self.union_array):
                if value == tmp:
                    self.union_array[i] = self.union_array[p]

    def is_connected(self, p, q):
        return self.union_array[p] == self.union_array[q]

    def is_one_union(self):
        return len(set(self.union_array)) == 1

    def __repr__(self):
        return 'QuickFind'


class QuickUnion:
    def __init__(self, n):
        self.n = n
        self.union_array = list(range(n))

    def root(self, i):
        while i != self.union_array[i]:
            i = self.union_array[i]
        return i

    def is_connected(self, i, j):
        return self.root(i) == self.root(j)

    def union(self, p, q):
        self.union_array[self.root(p)] = self.root(q)

    def is_one_union(self):
        tmp_root = self.root(self.union_array[0])
        return all([self.root(i) == tmp_root for i in self.union_array[1:]])

    def __repr__(self):
        return 'QuickUnion'


class QuickUnionWeighted(QuickUnion):
    def __init__(self, n):
        super().__init__(n)
        self.size_array = [1 for _ in range(n)]

    def union(self, p, q):
        p_root = self.root(p)
        q_root = self.root(q)
        if self.size_array[p_root] < self.size_array[q_root]:
            self.union_array[p_root] = q_root
            self.size_array[q_root] += self.size_array[p_root]
        else:
            self.union_array[q_root] = p_root
            self.size_array[p_root] += self.size_array[q_root]

    def __repr__(self):
        return 'QuickUnionWeighted'


class QuickUnionPathCompression(QuickUnionWeighted):
    def __init__(self, n):
        super().__init__(n)

    def root(self, i):
        while i != self.union_array[i]:
            self.union_array[i] = self.union_array[self.union_array[i]]
            i = self.union_array[i]
        return i

    def __repr__(self):
        return 'QuickUnionPathCompression'


def simulation(union, n, vertices):
    u = union(n)
    s = time.time()
    for pair in vertices:
        u.union(*pair)
    e = time.time()
    print(f'{u} took {e - s} seconds')


if __name__ == '__main__':
    n = 5 * 10 ** 4
    unions = [QuickFind, QuickUnion, QuickUnionWeighted, QuickUnionPathCompression]
    vertices = [np.random.randint(0, n, 2) for i in range(n)]
    with Pool(2) as pool:
        results = pool.starmap(simulation, ((union, n, vertices) for union in unions))
