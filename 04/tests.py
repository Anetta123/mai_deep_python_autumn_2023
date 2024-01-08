import unittest
from meta_class import CustomMeta, CustomClass
from descriptor import Integer, String, PositiveInteger, Data


class Meta_Test(unittest.TestCase):
    def setUp(self):
        self.tmp = CustomClass(50)
        self.tmp2 = CustomClass(200)
        self.tmp2.added_func = lambda x: x * 2

    def test_unintialized_meta(self):
        self.assertEqual(CustomClass.custom_x, 50)
        self.assertTrue(CustomClass.custom_line)
        self.assertEqual(CustomClass.custom_y, 50)

    def test_initialized_meta(self):
        self.assertEqual(self.tmp.custom_val, 50)
        self.assertEqual(self.tmp2.custom_val, 200)
        self.assertTrue(self.tmp2.custom_added_func)


class Descriptor_Test(unittest.TestCase):
    def test(self):
        self.assertTrue(Data(20, "Denis", 4000))
        with self.assertRaises(ValueError):
            Data(16, "Denis", 5000)
        with self.assertRaises(ValueError):
            Data(20, "Nia", 5000)
        with self.assertRaises(ValueError):
            Data(25, "Masha", 40000)
