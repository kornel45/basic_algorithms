# -*- coding: utf-8 -*-
"""
Module responsible for unit test coverage of union module
"""
from unittest import TestCase

from algorithms.Union.union import QuickUnionPathCompression, QuickFind, QuickUnion, QuickUnionWeighted


class TestQuickFind(TestCase):
    def setUp(self):
        self.u = QuickFind(5)

    def test_union_whenPNotConnectedWithQ_thenJoinsThem(self):
        self.u.is_connected = lambda x, y: False
        self.u.union(0, 1)
        self.assertEqual(self.u.union_array, [0, 0, 2, 3, 4])

    def test_union_whenPConnectedWithQ_thenPass(self):
        self.u.is_connected = lambda x, y: True
        self.u.union(0, 1)
        self.assertEqual(self.u.union_array, [0, 1, 2, 3, 4])

    def test_is_connected_whenTrue_thenReturnTrue(self):
        self.u.union_array = [0, 0, 2, 3, 4]
        result = self.u.is_connected(0, 1)
        self.assertTrue(result)

    def test_is_connected_whenFalse_thenReturnFalse(self):
        self.u.union_array = [0, 1, 2, 3, 4]
        result = self.u.is_connected(0, 1)
        self.assertFalse(result)


class TestQuickUnion(TestCase):
    def setUp(self):
        self.u = QuickUnion(5)

    def test_union_whenNotConnected_thenJoinsQRootToPRoot(self):
        self.u.union_array[1] = 2
        self.u.union(0, 1)
        self.assertEqual(self.u.union_array, [2, 2, 2, 3, 4])

    def test_union_whenConnected_thenPass(self):
        self.u.union(0, 1)
        self.assertEqual(self.u.union_array, [1, 1, 2, 3, 4])

    def test_is_connected_whenConnected_thenReturnTrue(self):
        self.u.union_array = [1, 1, 2, 3, 4]
        result = self.u.is_connected(0, 1)
        self.assertTrue(result)

    def test_is_connected_whenNotConnected_thenReturnFalse(self):
        self.u.union_array = [0, 1, 2, 3, 4]
        result = self.u.is_connected(0, 1)
        self.assertFalse(result)

    def test_root_whenIRoot_thenReturnI(self):
        self.assertEqual(self.u.root(2), 2)

    def test_root_whenJRoot_thenReturnJ(self):
        self.u.union_array = [0, 3, 2, 0, 4]
        j, i = 0, 1
        self.assertEqual(self.u.root(i), j)


class TestQuickUnionWeighted(TestCase):
    def setUp(self):
        self.u = QuickUnionWeighted(5)

    def test_union(self):
        pass


class TestQuickUnionPathCompression(TestCase):
    def setUp(self):
        self.u = QuickUnionPathCompression(5)

    def test_union(self):
        pass
