import errors

class Matrix:
    def __init__(self):
        self.matrix = [] # A two D array to represent the matrix.
        self.dimention = (len(self.matrix), len(self.matrix[0]))
    def __add__(self, other):
        if self.dimention == other.dimention:
            pass
        else:
            raise DimentionMismatch()
