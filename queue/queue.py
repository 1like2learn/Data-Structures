"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def dequeue(self):
#         if self.size > 0:
#             value = self.storage[0]
#             self.storage.pop(0)
#             self.size -= 1
#             return value

class Node:
    def __init__(self, value = None):
        self.value = value
        self.nextValue = None
class LinkedList:
    def __init__(self, headValue = None):
        self.headValue = headValue

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        endOfQueue = self.storage.headValue
        self.storage.headValue = Node(value)
        self.storage.headValue.nextValue = endOfQueue
        self.size += 1

    def dequeue(self):
        curVal = self.storage.headValue
        lastNode = None
        if curVal is None:
            return None
        elif curVal.nextValue is None:
            lastNode = curVal
            self.size -= 1
            self.storage.headValue = None
            return lastNode.value
        else:
            self.size -= 1
            lastVal = curVal
            while curVal.nextValue:
                curVal = curVal.nextValue
                if curVal.nextValue:
                    lastVal = curVal
            lastVal.nextValue = None
            return curVal.value

