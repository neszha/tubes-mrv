# import numpy as np
#
# A = np.array(([1,2],
#               [3,4]))
#
# B = np.array(([1,1],
#               [1,1]))

class Matrix:
    def __init__(self, use):
        self.data = []

    def set(self, a):
        self.data = a

    def show(self):
        print(self.data)


ini1 = Matrix(True)
ini1.set([1,2,3,4,5])
ini1.show()


ini2 = Matrix(True)
ini2.show()
ini1.show()
