from src.structures.node import Node

class stack:

    # EXP:       |_____|
    #            |__5__| -> top
    #            |__3__|
    #            |__8__|
    #            |__6__|
    #            size = 4

    # attributes of stack
    def __init__(self):
        self.top = None
        self.size = 0

    # push something in the stack
    def push(self, x):
        temp = Node(x)
        temp.next = self.top
        self.top = temp
        self.size += 1

    # remove the top node of the stack and return it
    # LIFO method
    def pop(self):
        if self.is_empty():
            return None
        popped = self.top
        self.top = popped.next
        self.size -= 1
        return popped.data

    # return True if sstack is empty and return False otherwise
    def is_empty(self):
        return self.size == 0

    # get the top node of the stack
    def get_top(self):
        if self.is_empty():
            return None
        return self.top.data


