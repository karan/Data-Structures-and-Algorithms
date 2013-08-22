# Dense Matrix
# @author: Karan Goel

class DenseMatrix(Matrix):

    def __init__(self, rows, cols):
        super(DenseMatrix, self).__init__(rows, cols)
        self._array = MultiDimensionalArray(rows, cols)

    def __getitem__(self, (i, j)):
        return self._array[i, j]

    def __setitem__(self, (i, j), value):
        self._array[i, j] = value
