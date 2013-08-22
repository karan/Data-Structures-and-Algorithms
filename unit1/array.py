# Arrays
# @author: Karan Goel

class Array(object):

    def __init__(self, length=0, baseIndex=0):
        """Initialize an empty array.
        length = length of array, baseIndex = lower bound for array indices
        """
        assert length >= 0
        self._data = [None for i in xrange(length)]
        self._baseIndex = baseIndex

    def __copy__(self):
        """Return a "shallow" copy of the given array."""
        result = Array(len(self._data))
        for i, datum in enumerate(self._data):
            result._data[i] = datum
        result._baseIndex = self.baseIndex
        return result

    def getOffset(self, index):
        """Translates given index into array's index"""
        offset = index - self._baseIndex
        if offset < 0 or offset >= len(self._data):
            raise IndexError
        return offset
        
    def __getitem__(self, index):
        """Return item at the given index"""
        return self._data[self.getOffset(index)]

    def __getitem__(self, index, value):
        """Set item at given index"""
        self._data[self.getOffset(index)] = value

    def getData(self):
        """Return the array's data"""
        return self._data

    data = property(fget=lambda self: self.getData())

    def getBaseIndex(self):
        """Returns the baseIndex of array"""
        return self._baseIndex

    def setBaseIndex(self, baseIndex):
        """Set the array's baseIndex to be given baseIndex"""
        self._baseIndex = baseIndex

    baseIndex = property(fget=lambda self: self.getBaseIndex(),
                         fset=lambda self, value: self.setBaseIndex(value))

    def __len__(self):
        return len(self._data)

    def setLength(self, value):
        """Resize the array"""
        if len(self._data) != value:
            newData = [None for i in xrange(value)]
            m = min(len(self._data), value)
            for i in xrange(m):
                newData[i] = self._data[i]
            self._data = newData

    length = property(fget=lambda self: self.__len(),
                      fset=lambda self, value: self.setLength(value))
