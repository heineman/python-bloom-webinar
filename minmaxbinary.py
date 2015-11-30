"""
    Create Binary Search Tree where each node stores the
    minimum and maximum value within its subtree to support
    Fast-Fail for contains when possible.

    Contains method returns False immediately if not possible
    to be in the list, based on these values.

    Author: George Heineman    
"""
class MinMaxBinaryNode:

    def __init__(self, value):
        """Create binary node."""
        self.value   = value
        self.left    = None
        self.right   = None
        self.min     = value
        self.max     = value

    def add(self, val):
        """
        Add a new node to the tree with value. Respond based on Set semantics
        """
        if val <= self.value:
            self.left = self.addToSubTree(self.left, val)
            self.min = self.left.min
        elif val > self.value:
            self.right = self.addToSubTree(self.right, val)
            self.max = self.right.max

    def addToSubTree(self, parent, val):
        """Add val to parent subtree (if exists) and return root of that subtree."""
        if parent is None:
            return MinMaxBinaryNode(val)

        parent.add(val)
        if parent.left:
            parent.min = min(parent.min, parent.left.min)
        if parent.right:
            parent.max = max(parent.max, parent.right.max)
        return parent

    def remove(self, val):
        """
         Remove val of self from BinaryTree. 
        """
        if val < self.value:
            self.left = self.removeFromParent(self.left, val)
            if self.left:
                self.min = self.left.min
            else:
                self.min = self.value
        elif val > self.value:
            self.right = self.removeFromParent(self.right, val)
            if self.right:
                self.max = self.right.max
            else:
                self.max = self.value
        else:
            if self.left is None:
                return self.right

            child = self.left
            while child.right:
                child = child.right
            
            childKey = child.value;
            self.left = self.removeFromParent(self.left, childKey)
            self.value = childKey;
        
        return self

    def removeFromParent(self, parent, val):
        """Helper method for remove. Ensures proper behavior when removing node that 
        has children."""
        if parent:
            parent = parent.remove(val)
            if parent:
                if parent.left:
                    parent.min = min(parent.min, parent.left.min)
                if parent.right:
                    parent.max = max(parent.max, parent.right.max)
        return None

    def __repr__(self):
        """Useful debugging function to produce linear tree representation."""
        
        return "(min:" + str(self.min) + " " + str(self.value) + " max:" + str(self.max) + ")"


class MinMaxBinaryTree:

    def __init__(self):
        """Create empty binary tree."""
        self.root = None
   
    def add(self, value):
        """Insert value into proper location in Binary Tree."""
        if self.root is None:
            self.root = MinMaxBinaryNode(value)
        else:
            self.root.add(value)

    def remove(self, val):
        """Remove value from tree."""
        if self.root:
            self.root = self.root.remove(val)

    
    def __contains__(self, target):
        """Check whether BST contains target value."""
        node = self.root
        while node:
            if target < node.min or target > node.max:
                return False
            
            if target < node.value :
                node = node.left
            elif target > node.value:
                node = node.right
            else:
                return True
                
        return False


    def __repr__(self):
        if self.root is None:
            return "binary:()"
        return "binary:" + str(self.root)

"""
Change Log:
-----------

"""
