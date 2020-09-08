"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        #Store oldHead so we can link it to the new value
        oldHead = self.head
        #Make sure our length is up to date
        self.length += 1
        #If oldHead exists make a new node with provided value and
        #a link to oldHead
        if oldHead:
            newHead = ListNode(value, None, oldHead)
            oldHead.prev = newHead
            self.head = newHead
        #Otherwise the list was empty before and make a node that 
        #doesn't lead anywhere
        else:
            self.head = ListNode(value)
            self.tail = self.head
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        #Check if the list actually has anything
        if self.length > 0:
        #Store oldHead so we can link stuff
            oldHead = self.head
        #If there's only one link make the list empty
            if self.length == 1:
                self.head = None
                self.tail = None
        #Otherwise make oldHead's next item the head and
        #unlink it from oldHead
            else:
                newHead = oldHead.next
                newHead.prev = None
                self.head = newHead
        #adjust length
            self.length -= 1
        #return value
            return oldHead.value

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        #Store oldTail so we can link stuff
        oldTail = self.tail
        #Adjust length
        self.length += 1
        #If the list is not empty connect the new node to oldTail
        #and make the new node the tail
        if oldTail:
            newTail = ListNode(value, oldTail, None)
            oldTail.next = newTail
            self.tail = newTail
        #If the list is empty assign a new node to tail and head
        else:
            self.tail = ListNode(value)
            self.head = self.tail
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        #If the list is not empty
        if self.length > 0:
        #Store oldLast for later
            oldLast = self.tail
        #If there is only one item in the list make the list empty
            if self.length == 1:
                self.head = None
                self.tail = None
        #Otherwise make oldLast's previous node the new tail
            else:
                newLast = oldLast.prev
                newLast.next = None
                self.tail = newLast
        #Adjust the length
            self.length -= 1
        #Return the value of the old tail
            return oldLast.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        #Connect node's neighbors to each other and check
        #to make sure node is not at the end of the list
        targetPrev = node.prev
        targetNext = node.next
        if not targetPrev:
            targetNext.prev = None
        elif not targetNext:
            targetPrev.next = None
        else:
            targetPrev.next = targetNext
            targetNext.prev = targetPrev
        #Take the old head and tack it on the end of node
        oldHead = self.head
        node.next = oldHead
        #Make sure node has no previous node
        node.prev = None
        #Make node the head
        self.head = node
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        #If the list is only 1 long do nothing
        if self.length == 1:
            return
        #If node is the head reasign head
        elif self.head is node:
            self.head = self.head.next
            self.head.prev = None
        #Otherwise assign the previous node to the next node and
        #vice versa
        else:
            targetPrev = node.prev
            targetNext = node.next
            targetNext.prev = targetPrev
            targetPrev.next = targetNext
        #Add node to the end of oldTail
        oldTail = self.tail
        oldTail.next = node
        #Assign the oldTail to node's previous
        node.prev = oldTail
        #Make node.next point to nothing
        node.next = None
        #Make the tail point to node
        self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        #Make sure the list isn't empty
        if self.length > 0:
        #Connect node's neighbors to each other and check
        #to make sure node is not at the begginning of the list
            targetPrev = node.prev
            targetNext = node.next
        #If there's only one item make the list empty
            if self.length == 1:
                self.head = None
                self.tail = None
        #If the node is the head reassign the head
            elif self.head is node:
                self.head = self.head.next
        #If the node is the tail reassign the tail
            elif self.tail is node:
                self.tail = self.tail.prev
        #Otherwise link the target's prev and next to each other
            else:
                targetNext.prev = targetPrev
                targetPrev.next = targetNext
        #Adjust the length
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        #Store a current value to iterate starting with the head
        #Store a maxVal to increase if curVal is greater
        curVal = self.head
        maxVal = 0
        if self.length == 1:
            maxVal = curVal.value
        while curVal:
            if curVal.value > maxVal:
                maxVal = curVal.value
            curVal = curVal.next
        #Return the maxVal in the list
        return maxVal
