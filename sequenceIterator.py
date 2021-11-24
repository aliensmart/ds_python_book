class SequenceIterator:
    """An Iterator for any of Python's sequence types."""
    
    def __init__(self, sequence):
        """Create an iterator fo the given sequence"""
        self._seq = sequence # keep a reference to the underlying data
        self._k = -1  # will increment to 0 on ﬁrst call to next
        
    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k += 1  # Advance to next index
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()
        
    def __iter__(self):
        """By convention, an iterator must return itsefl as an iterator."""
        return self
        
        
        