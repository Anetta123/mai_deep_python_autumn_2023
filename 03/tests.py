from main import CustomList
import unittest


class ListTest(unittest.TestCase):
    """List test class"""

    def setUp(self):
        self.list1 = CustomList([1, 2, 3])
        self.list2 = CustomList([1, 2, 3, 4, 5, 6])
        self.list3 = CustomList([0, 0])
        self.list4 = CustomList([-2, 0, 1, 2, 3])
        self.list5 = CustomList([])

    def test_add(self):
        res1 = self.list1 + self.list2
        res2 = self.list2 + self.list3
        res3 = self.list5 + self.list5
        res4 = self.list4 + self.list1
        self.assertEqual(res1, [2, 4, 6, 4, 5, 6])
        self.assertEqual(res2, [1, 2, 3, 4, 5, 6])
        self.assertEqual(res3, [])
        self.assertEqual(res4, [-1, 2, 4, 2, 3])

    def test_substrction(self):
        res1 = self.list1 - self.list2
        res2 = self.list2 - self.list4
        res3 = self.list3 - self.list5
        res4 = self.list4 - self.list2
        self.assertEqual(res1, [0, 0, 0, -4, -5, -6])
        self.assertEqual(res2, [3, 2, 2, 2, 2, 6])
        self.assertEqual(res3, [0, 0])
        self.assertEqual(res4, [-3, -2, -2, -2, -2, -6])

    def test_comparison(self):
        self.assertTrue(self.list2 > self.list1)
        self.assertFalse(self.list1 < self.list5)
        self.assertTrue(self.list1 == self.list1)
        self.assertTrue(self.list4 <= self.list2)
        self.assertFalse(self.list2 < self.list1)

    def test_ordinary_list(self):
        self.assertEqual(self.list1 + [1, 2, 3], [2, 4, 6])
        self.assertEqual(self.list2 - [0, 0, 0, 1, 10, 3], [1, 2, 3, 3, -5, 3])
        self.assertEqual([1, 4, 1, 4] - self.list4, [3, 4, 0, 2, -3])
