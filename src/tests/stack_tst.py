import unittest
from src.structures.stack import stack

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = stack()

    def test_push_one(self):
        self.stack.push(1)
        self.assertEqual(self.stack.top.data, 1)
        self.assertEqual(self.stack.size, 1)
        self.assertIsNone(self.stack.top.next)

    def test_push_more(self):
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(8)
        self.assertEqual(self.stack.size, 3)
        self.assertEqual(self.stack.top.data, 8)
        self.assertEqual(self.stack.top.next.data, 3)
        self.assertEqual(self.stack.top.next.next.data, 2)

    def test_is_empty(self):
        self.assertEqual(self.stack.is_empty() , True)
        self.stack.push(1)
        self.assertEqual(self.stack.is_empty() , False)

    def test_top(self):
        self.assertEqual(self.stack.get_top(), None)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.get_top(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.get_top(), 1)

    def test_pop(self):
        self.assertEqual(self.stack.pop(), None)
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.pop()
        self.assertEqual(self.stack.top.data , 2)
        self.assertEqual(self.stack.size, 2)

if __name__ == '__main__':
    unittest.main()
