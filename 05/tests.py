import unittest
from LRUcache import LRUCache
from DoubleLinkedList import Node


class lrucache_test(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(5)

    def test_case_empty(self):
        self.assertEqual(self.cache.get("1"), None)
        self.assertEqual(self.cache.get("2"), None)

    def test_set_get(self):
        self.cache.set("1", "1")
        self.assertEqual(self.cache.get("1"), "1")
        self.cache.set("2", "2")
        self.cache.set("3", "3")
        self.cache.set("4", "4")
        self.cache.set("5", "5")
        self.assertEqual(self.cache.get("5"), "5")
        self.cache.set("6", "6")
        self.assertEqual(self.cache.get("1"), None)
        self.assertEqual(self.cache.get("6"), "6")

