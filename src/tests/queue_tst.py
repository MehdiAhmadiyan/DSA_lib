import unittest
from src.structures.queue import queue


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.queue = queue()

    def test_push_one(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.head.data, 1)
        self.assertEqual(self.queue.size, 1)

    def test_push_more(self):
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.assertEqual(self.queue.head.data, 2)
        self.assertEqual(self.queue.size, 3)

    def test_dequeue(self):
        self.assertEqual(self.queue.dequeue(), None)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue() , 2)
        self.assertEqual(self.queue.size, 1)

    def test_is_empty(self):
        self.assertEqual(self.queue.size, True)
        self.queue.enqueue()
        self.assertEqual(self.queue.size, False)

    def test_head(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.head(), self.queue.head.data)
        self.queue.dequeue()
        self.assertEqual(self.queue.head(), self.queue.head.data)

if __name__ == '__main__':
    unittest.main()
