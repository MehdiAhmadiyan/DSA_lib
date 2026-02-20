from src.structures.node import Node

class stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, x):
        temp = Node(x)
        temp.next = self.top
        self.top = temp
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        popped = self.top
        self.top = popped.next
        self.size -= 1
        return popped.data

    def is_empty(self):
        return self.size == 0

    def get_top(self):
        if self.is_empty():
            return None
        return self.top.data


