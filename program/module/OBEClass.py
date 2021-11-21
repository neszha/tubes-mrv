# import numpy as np
# import module.console as console
# import module.init as Route

# Object untuk menghanddle operasi OBE.
# #
class OBE:
    # Constructor method.
    def __init__(self, matrix):
        self.matrix = matrix

    def gauss(self):
        print('\n')
        [row, col] = self.matrix.shape

        print(self.matrix, '\n')
        for i in range(0, 1):
            # Mencari nilai 0 untuk dilakukan pivoting ke bawah.
            for j in range(row):
                elm = self.matrix[j][i]
                if elm == 0:
                    self.pivoting(j, row - 1)

            # Mencari nilai 1 untuk dilakukan pivoting ke atas.
            for j in range(row):
                elm = self.matrix[j][i]
                if elm == 1:
                    self.pivoting(j, i)

            # Membuat 1 utama.
            elm_point = self.matrix[i][i]
            if elm_point != 1 or elm_point != 0:
                for j in range(i, col):
                    print('make 1:', self.matrix[i][j], elm_point)
                    self.matrix[i][j] /= elm_point
            print('\n', self.matrix)

            print('')
            # Membuat element di bahwa 1 bernilai 0.
            next_row = i + 1;
            for j in range(i + 1, row):
                elm_up = self.matrix[i]
                for k in range(col):
                    elm = self.matrix[j][k]
                    print('make 0:', elm, elm_up[k])
                    self.matrix[j][k] -= elm * elm_up[k]

        print('\n', self.matrix)
        print('belum kelar')
            # break

    def gauss_jordan(self):
        print('gauss_jordan')

    def pivoting(self, from_row, to_row):
        if from_row == to_row:
            return True
        print('pivoting', from_row, to_row)
        temp_row = self.matrix[to_row].copy()
        self.matrix[to_row] = self.matrix[from_row]
        self.matrix[from_row] = temp_row
        print(self.matrix)
