"""
    Store one-dimensional vector of non-negative
    integer values. If val[n] is 0, then n does
    not exist in the collection, otherwise it does.

    Author: George Heineman    
"""

class Storage :

    def __init__(self):
        self.data = []
        self.size = 0

    def add (self, val):
        """Insert element val."""
        if val < 0:
            raise "Storage only supports non-negative integers" 
        if self.size < val:
            self.data += ([False]*(val - self.size + 1))
            self.size = len(self.data)
        self.data[val] = True
    
    def remove(self, val):
        """Remove val."""

        # not present. Nothing to do
        if val < 0 or val >= self.size:
            return 
        self.data[val] = False
    
    def __contains__(self, val):
        """Determine whether contains val."""
        if val < 0 or val >= self.size:
            return False
        
        return self.data[val]

"""
Change Log:

"""

