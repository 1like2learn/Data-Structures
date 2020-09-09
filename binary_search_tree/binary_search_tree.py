"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #Dim current node and whether or not the loop should continue
        node = self
        loop = True
        while loop:
        #If the node value is greater than the new value check if node.left exists
        #If it exists make it the new node and loop again. Otherwise set a new node
        #with the new value and end the loop
            if node.value > value:
                if node.left:
                    node = node.left
                else:
                    node.left = BSTNode(value)
                    loop = False
        #If the node value is less than the new value check if node.right exists
        #If it exists make it the new node and loop again. Otherwise set a new node
        #with the new value and end the loop
            elif node.value <= value:
                if node.right:
                    node = node.right
                else:
                    node.right = BSTNode(value)
                    loop = False
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        node = self
        loop = True
        #Loop until we reach the end of the tree
        while loop:
        #If the target is less than node
            if node.value > target:
        #Reassign node if node.left exists
                if node.left:
                    node = node.left
        #Otherwise return false
                else:
                    return False
        #If the target is greater than node
            elif node.value < target:
        #Reassign node if node.left exists
                if node.right:
                    node = node.right
        #Otherwise return false
                else:
                    return False
        #If node equals the target return true
            elif node.value == target:
                return True

    # Return the maximum value found in the tree
    def get_max(self):
        #Assign current node
        node = self
        #While node.right exists assign node to node.right
        while node.right:
            node = node.right
        #Once we have the greatest value for node return node.value
        return node.value
            
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

        # #Dim a list of nodes to check
        # workList = [self]
        # #Check that the list isn't empty
        # while len(workList) > 0:
        # #Assign the first value in the list to node
        #     node = workList[0]
        # #If node.left exists add it to the worklist
        #     if node.left:
        #         workList.append(node.left)
        # #If node.right exists add it to the worklist
        #     if node.right:
        #         workList.append(node.right)
        # #Use the provided function on the node value
        # #and remove the node from the workList
        #     fn(node.value)
        #     workList.remove(node)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        #If self exists
        if self:
        #If self doesn't have a lower value print it
            if not self.left:
                print(self.value)
        #Otherwise run the function again with it's left path
            else:
                self.left.in_order_print()
                print(self.value)
            
            if self.right:
                self.right.in_order_print()
    """
                    1
                        8
                    5
                3       7
            2      4 6

    """
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        #Dim a list of nodes to check
        workList = [self]
        #Check that the list isn't empty
        while len(workList) > 0:
        #Assign the first value in the list to node
            node = workList[0]
        #If node.left exists add it to the worklist
            if node.left:
                workList.append(node.left)
        #If node.right exists add it to the worklist
            if node.right:
                workList.append(node.right)
        #Print the value and remove the node from the workList
            print(node.value)
            workList.remove(node)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # print(self.value)
        # if self.left:
        #     self.left.dft_print()
        # if self.right:
        #     self.right.dft_print()

        #Dim a list of nodes to check
        workList = [self]
        #Check that the list isn't empty
        while len(workList) > 0:
        #Assign the last value in the list to node
            node = workList[-1]
        #If node.left exists add it to the worklist
            if node.left:
                workList.append(node.left)
        #If node.right exists add it to the worklist
            if node.right:
                workList.append(node.right)
        #Print the value and remove the node from the workList
            print(node.value)
            workList.remove(node)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
print("\nbft_print")
bst.bft_print()
print("\ndft_print")
bst.dft_print()

print("elegant methods")
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft() 
print("pre order")
bst.pre_order_dft() 