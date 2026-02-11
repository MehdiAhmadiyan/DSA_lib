from src.structures.node import Node

class stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, x):
        temp = Node(x)
        temp.next = self.top
        temp.next.prev = temp
        self.top = temp
