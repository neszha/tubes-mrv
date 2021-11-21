# Object untuk menghanddle operasi OBE.
# #
class OBE:
    # Constructor method.
    def __init__(self, matrix):
        self.matrix = matrix

    # Melakukan eliminasi gauss pada matriks argumented.
    def gauss(self):
        [row, col] = self.matrix.shape

        for i in range(0, min(row, col)):
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
                    self.matrix[i][j] /= elm_point

            # Membuat element di bawah 1 bernilai 0.
            for j in range(i + 1, row):
                elm_poin = 0
                elms_up = self.matrix[i]
                elms_point = self.matrix[j]

                # Mencari element sebagai titik perhitungan.
                for a in range(len(elms_point)):
                    if elms_point[a] != 0:
                        elm_poin = elms_point[a]
                        break;

                # Melakukan operasi OBE pada kolom.
                for k in range(col):
                    self.matrix[j][k] -= elm_poin * elms_up[k]

        return self.matrix

    # Melakukan eliminasi gauss jordan pada matriks argumented.
    def gauss_jordan(self):
        # Malakukan OBE gauss.
        self.gauss();

        # Melanjutkan menjadi gauss jordan.
        [row, col] = self.matrix.shape

        for i in range(1, min(row, col)):
            # Membuat element di atas 1 bernilai 0.
            for j in range(0, i):
                elm_poin = 0
                elms_up = self.matrix[j]
                elms_point = self.matrix[i]

                # Mencari element sebagai titik perhitungan.
                elm_poin = 0
                for a in range(len(elms_up)):
                    if elms_up[a] != 1 and elms_up[a] != 0:
                        elm_poin = elms_up[a]
                        break;

                # Operasi eliminasi untuk membuat element 0.
                for k in range(col):
                    self.matrix[j][k] -= elm_poin * elms_point[k]

        return self.matrix

    # Melakukan pivoting atau pertukaran element kolom pada
    # matriks argumented.
    def pivoting(self, from_row, to_row):
        if from_row == to_row:
            return True
        temp_row = self.matrix[to_row].copy()
        self.matrix[to_row] = self.matrix[from_row]
        self.matrix[from_row] = temp_row
        print(self.matrix)
