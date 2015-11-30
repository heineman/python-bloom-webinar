"""
    Demonstrate Bloom filter using native python.
    
    Uses raw ints as the basis for bloom.
"""

class bloomFilter:
    def __init__(self, size = 1000, hashFunctions=None):
        """
        Construct a bloom filter with size bits (default: 1000) and the associated hash functions.
        If no hash functions are provided, then a single function based on hash(e) % size is used.
        """
        self.bits = 0  
        self.M = size
        if hashFunctions is None:
            self.k = 1
            self.hashFunctions = [lambda e, size : hash(e) % size]
        else:
            self.k = len(hashFunctions)
            self.hashFunctions = hashFunctions
            
    def add(self, value):
        """Insert value into the bloom filter."""
        for hf in self.hashFunctions:
            self.bits |= 1<<hf(value, self.M)
            
    def countbits(self):
        """Count the number of bits set in the bloom filter."""
        n = self.bits
        num = 0
        while n > 0:
            num += (n % 2)
            n = n >> 1
        return num
            
    def fingerprint(self, value):
        """Return hash indices for the given value. Useful for debugging."""
        return [hf(value, self.M) for hf in self.hashFunctions]
         
    def __contains__(self, value):
        """
        Determine whether value is present. A false positive might be returned even if the 
        element is not present. However, a false negative will never be returned (that is, 
        if the element is present, then it will return True).
        """
        for hf in self.hashFunctions:
            if self.bits & 1<<hf(value, self.M) == 0:
                return False
        
        # might be present
        return True
