from src.structures.trees.tree_node import TreeNode

class BinarySearchTree(TreeNode):
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent