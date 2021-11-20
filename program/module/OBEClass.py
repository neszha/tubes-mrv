# import numpy as np
# import module.console as console
# import module.init as Route

# Object untuk menghanddle operasi guass.
# #
class OBE:
    # Constructor method.
    def __init__(self, matrix):
        self.matrix = matrix

    def gauss(self):
        print('\n')
        [row, col] = self.matrix.shape

        for i in range(row):
            print(self.matrix[i])
        # print(self.matrix)

    def gauss_jordan(self):
        print('gauss_jordan')

    def pivoting(self):
        print('pivoting')
