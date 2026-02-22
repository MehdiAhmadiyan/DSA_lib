from src.structures.node import Node

class List:
    # EXP:  rear                                              front
    #       7     <->   8   <->   4   <->   8   <->   9   <->   11
    #       Size = 6

    # Attributes of a list
    def __init__(self):
        self.size = 0
        self.front = None
        self.rear = None

    # True if size is empty / False otherwise
    def is_empty(self):
        return self.size == 0

    # push at the end of the list
    # EXP: 4 <-> 3 <-> 8  ----push_back(1)---->>  4 <-> 3 <-> 8 <-> 1
    def push_back(self, data):
        # creating new node
        new_node = Node(data)
        #  if list is empty
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
            self.size = 1
            return

        #  joining new node to list
        self.rear.next = new_node
        new_node.prev = self.rear
        self.rear = new_node
        self.size += 1
        return

    # pop the end node of the list
    # EXP: 4 <-> 3 <-> 8 <-> 1  ----pop_back()--->>  4 <-> 3 <-> 8
    def pop_back(self):
        try:
            #  identify and pop the rear node
            del_node = self.rear
            self.rear = self.rear.prev
            self.rear.next = None
            self.size -= 1
            return del_node
        except Exception as e:
            # raises when list id empty
            raise e

    # push in front of the the list
    # EXP: 4 <-> 3 <-> 8  ----push_front(1)--->>  1 <-> 4 <-> 3 <-> 8
    def push_front(self, data):
        # creating new node
        new_node = Node(data)
        # if list is empty
        if self.is_empty():
            self.rear = new_node
            self.front = new_node
            self.size = 1
            return

        # if is not empty
        new_node.next = self.front
        self.front.prev = new_node
        self.front = new_node
        self.size += 1
        return

    # pop the front node of the list
    # EXP: 1 <-> 4 <-> 3 <-> 8  ----pop_front()--->>  4 <-> 3 <-> 8
    def pop_front(self):
        try:
            # if list is not empty
            del_node = self.front
            self.front = self.front.next
            self.front.prev = None
            self.size -= 1
            return del_node
        except Exception as e:
            #  raises if list is empty
            raise e

    # inserting a node in any place of the list. In given index
    # EXP: 4 <-> 3 <-> 8  ----insert(5 , 1)--->>   4 <-> 5 <-> 3 <-> 8
    def insert(self, data, index):
        # creating new node
        new_node = Node(data)
        #  Check if index is out of range
        if index < 0 or index > self.size:
            raise IndexError(f"Index {index} out of range [0, {self.size}]")

        if self.is_empty():
            # Check if list is empty
            self.front = new_node
            self.rear = new_node
            self.size = 1
        elif index == 0:
            # Check if index is front of the list
            self.push_front(data)
        elif index == self.size:
            # Check if index is rear of the list
            self.push_back(data)
        else:
            # inserting in middle of the list
            current = self.front
            for i in range(index - 1):
                # Iterate to the index. Its take O(1) time in worst case!
                current = current.next
            #  Setting links
            new_node.next = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next.prev = new_node
            self.size += 1
            return

    # Delete a node from any place of list with an index
    # EXP: 4 <-> 5 <-> 3 <-> 8   ----delete(5)--->> 4 <-> 3 <-> 8
    def delete(self, index):

        #  Check if index is out of range
        if index < 0 or index > self.size:
            raise IndexError(f"Index {index} out of range [0, {self.size}]")

        if self.is_empty():
            # Check if list is empty
            return None
        elif index == 0:
            # Check if index is front of the list
            self.pop_front()
        elif index == self.size:
            # Check if index is rear of the list
            self.pop_back()
        else:
            # Check if its in middle of the list
            current = self.front
            for i in range(index - 1):
                # Iterate to the index. Its take O(1) time in worst case!
                current = current.next
            # Setting links and delete node
            current.next = current.next.next
            current.next.prev = current
            self.size -= 1

    # get the front node of the list
    # EXP: 4 <-> 5 <-> 3 <-> 8  ----get_front()--->> 4
    def get_front(self):
        return self.front.data

    # get the rear node of the list
    # EXP: 4 <-> 5 <-> 3 <-> 8  ----get_rear()--->> 8
    def get_rear(self):
        return self.rear.data

    # get the size of the list
    # EXP: 4 <-> 5 <-> 3 <-> 8  ----get_size()--->> 4
    def get_size(self):
        return self.size

