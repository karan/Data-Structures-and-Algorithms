# Multi Dimensional Array
# @author: Karan Goel

class MultiDimensionalArray(object):

    def __init__(self, *dimensions):
        self._dimensions = Array(len(dimensions))
        self._factors = Array(len(dimensions))
        product = 1
        i = len(dimensions) - 1
        while i >= 0:
            self._dimensions[i] = dimensions[i]
            self._factors[i] = product
            product *= self._dimensions[i]
            i -= 1
        self._data = Array(product)

    def getOffset(self, indices):
        if len(indices) != len(self._dimensions):
            raise IndexError
        offset = 0
        for i, dim in enumerate(self._dimensions):
            if indices[i] < 0 or indices[i] >= dim:
                raise IndexError
            offset += self._factors[i] * indices[i]
        return offset

    def __getitem__(self, indices):
        return self._data[self._getOffset(indices)]

    def __setitem__(self, indices, value):
        self._data[self._getOffset(indices)] = value
