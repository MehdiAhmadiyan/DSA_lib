import unittest
from src.structures.trees.bst import BinarySearchTree

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.tree = BinarySearchTree()
    def test_insert(self):
        self.tree.insert(5)
        self.assertEqual(self.tree.root.data, 5)
        self.assertEqual(self.tree.root.left, None)
        self.assertEqual(self.tree.root.right, None)
        self.assertEqual(self.tree.size, 1)
        self.insert(7)
        self.assertEqual(self.tree.root.left, None)
        self.assertEqual(self.tree.root.right.data, 7)
        self.assertEqual(self.tree.root.right.left, None)
        self.assertEqual(self.tree.root.right.right, None)
        self.assertEqual(self.tree.size, 2)
        self.insert(6)
        self.assertEqual(self.tree.root.right.left.data, 6)

if __name__ == '__main__':
    unittest.main()
