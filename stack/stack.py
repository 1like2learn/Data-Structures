"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
    # def __init__(self):
    #     self.size = 0
    #     self.storage = []

    # def __len__(self):
    #     return len(self.storage)

    # def push(self, value):
    #     self.storage.append(value)

    # def pop(self):
    #     if len(self.storage) > 0:
    #         value = self.storage[-1]
    #         self.storage.pop(-1)
    #         return value

class Node:
    def __init__(self, value = None):
        self.value = value
        self.nextValue = None
class LinkedList:
    def __init__(self, headValue = None):
        self.headValue = headValue

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        oldTop = self.storage.headValue
        self.storage.headValue = Node(value)
        self.storage.headValue.nextValue = oldTop
        self.size += 1

    def pop(self):
        if self.storage.headValue is None:
            return None
        oldTop = self.storage.headValue
        self.storage.headValue = oldTop.nextValue
        self.size -= 1
        return oldTop.value
