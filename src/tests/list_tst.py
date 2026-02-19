import unittest
from src.structures.list import List

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.list = List()
    def test_push_front(self):
        self.list.push_front(5)
        self.list.push_front(7)
        self.assertEqual(self.list.size, 2)
        self.assertEqual(self.list.front.data, 7)
        self.assertEqual(self.list.rear.data, 5)

    def test_is_empty(self):
        self.assertEqual(self.list.is_empty(), True)
        self.list.push_front(5)
        self.assertEqual(self.list.is_empty(), False)

    def test_pop_front(self):
        with self.assertRaises(Exception):  # یا IndexError
            self.list.pop_front()
        self.list.push_front(5)
        self.list.push_front(7)
        self.list.push_front(3)
        self.list.pop_front()
        self.assertEqual(self.list.size, 2)
        self.assertEqual(self.list.front.data, 7)
        self.assertEqual(self.list.rear.data, 5)
        self.list.pop_front()
        self.assertEqual(self.list.size, 1)
        self.assertEqual(self.list.front.data, self.list.rear.data)

    def test_push_back(self):
        self.list.push_back(5)
        self.assertEqual(self.list.size, 1)
        self.assertEqual(self.list.rear.data, 5)
        self.list.push_back(7)
        self.assertEqual(self.list.size, 2)
        self.assertEqual(self.list.rear.data, 7)
        self.assertEqual(self.list.front.data, 5)
    def test_pop_back(self):
        with self.assertRaises(Exception):
            self.list.pop_back()

        self.list.push_back(5)
        self.list.push_back(7)
        self.list.push_back(3)
        self.list.pop_back()
        self.assertEqual(self.list.size, 2)
        self.assertEqual(self.list.rear.data, 7)
        self.assertEqual(self.list.front.data, 5)
    def test_insert(self):
        with self.assertRaises(IndexError):
            self.list.insert(10, 5)

        self.list.push_back(5)
        self.list.push_back(7)
        self.list.push_back(3)
        self.list.insert(2, 1)
        self.assertEqual(self.list.size, 4)
        self.assertEqual(self.list.front.next.data, 2)
        self.list.insert(6 , 4)
        self.assertEqual(self.list.size, 5)
        self.assertEqual(self.list.rear.data, 6)
    def test_delete(self):
        with self.assertRaises(IndexError):
            self.list.delete(5)

        self.list.push_back(5)
        self.list.push_back(7)
        self.list.push_back(3)
        self.list.push_back(1)
        self.list.delete(2)
        self.assertEqual(self.list.size, 3)
        self.assertEqual(self.list.rear.prev.data, 7)
        self.assertEqual(self.list.front.next.data, 7)
    def test_front(self):
        with self.assertRaises(Exception):
            self.list.get_front()

        self.list.push_back(5)
        self.list.push_back(7)
        self.list.push_back(3)
        self.assertEqual(self.list.get_front(), self.list.front.data)
    def test_rear(self):
        with self.assertRaises(Exception):
            self.list.get_rear()

        self.list.push_back(5)
        self.list.push_back(7)
        self.list.push_back(3)
        self.assertEqual(self.list.get_rear(), self.list.rear.data)
    def test_size(self):
        self.assertEqual(self.list.get_size(), 0)
        self.list.push_back(5)
        self.list.push_back(7)
        self.assertEqual(self.list.get_size(), self.list.size)

    """  TO DO:
    add this functios:
def clear(self):              # پاک کردن کل لیست
def find(self, value):        # پیدا کردن اولین مقدار
def find_all(self, value):    # پیدا کردن همه مقادیر
def contains(self, value):    # بررسی وجود مقدار
def get(self, index):         # دریافت مقدار در ایندکس مشخص
def set(self, index, value):  # تغییر مقدار در ایندکس مشخص
def reverse(self):            # معکوس کردن لیست
def to_list(self):            # تبدیل به لیست پایتون
def print_forward(self):      # چاپ از اول به آخر
def print_backward(self):     # چاپ از آخر به اول"""

if __name__ == '__main__':
    unittest.main()
