# Object untuk menghanddle operasi OBE.
# #
class OBE:
    # Constructor method.
    def __init__(self, matrix):
        self.matrix = matrix
        self.matrix_origin = matrix.copy()
        self.with_method = None
        self.solution = None

    # Mengambil hasil persamaan dari persamaan matriks argumented.
    def get_solution(self):
        if self.with_method == 'gaus':
            self.generate_solution_gauss()
        elif self.with_method == 'gauss_jordan':
            self.generate_solution_gauss_jordan()
        return self.solution

    # Melakukan eliminasi gauss pada matriks argumented.
    def gauss(self):
        self.with_method = 'gauss'
        [row, col] = self.matrix.shape
        size = min(row, col)

        for i in range(size):
            # Mencari nilai 1 untuk dilakukan pivoting ke atas.
            for j in range(i, size):
                elm = self.matrix[j][i]
                if elm == 1:
                    self.pivoting(j, i)
                    break

            # Mencari titik element 1 utama.
            elm_point = 1
            for j in range(i, col):
                elm = self.matrix[i][j]
                if elm != 0:
                    elm_point = elm;
                    break

            # Membuat element 1 utama.
            for j in range(i, col):
                self.matrix[i][j] /= elm_point

            # Membuat element di bawah 1 bernilai 0.
            for j in range(i + 1, size):
                ratio = self.matrix[j][i] / self.matrix[i][i]
                for k in range(size + 1):
                    self.matrix[j][k] -= ratio * self.matrix[i][k]

        return self.matrix

    # Melakukan eliminasi gauss jordan pada matriks argumented.
    def gauss_jordan(self):
        # Malakukan OBE gauss.
        self.gauss();

        # Melanjutkan menjadi gauss jordan.
        self.with_method = 'gauss_jordan'
        [row, col] = self.matrix.shape
        # size = min(row, col)
        size = 2

        for i in range(0, size):
            # Membuat element di atas 1 bernilai 0.
            for j in range(0, i):
                # Mencari titik di samping element 1 utama.
                elm_point = 1
                for j in range(i, col):
                    elm = self.matrix[i - 1][j]
                    if elm != 0:
                        elm_point = elm;
                        break

                # Operasi eliminasi untuk membuat element 0.
                for j in range(col):
                    print(elm_point, self.matrix[i][j])
                    # self.matrix[j][k] -= elm_poin * elms_point[k]

                # print(elm_point)

                # elms_up = self.matrix[j]
                # elms_point = self.matrix[i]

                # Mencari element sebagai titik perhitungan.
                # elm_poin = 1
                # for a in range(len(elms_up)):
                #     if elms_up[a] != 1 and elms_up[a] != 0:
                #         elm_poin = elms_up[a]
                #         break;

                # Operasi eliminasi untuk membuat element 0.
                # for k in range(col):
                    # self.matrix[j][k] -= elm_poin * elms_point[k]

        return self.matrix

    # Melakukan pivoting atau pertukaran element kolom pada
    # matriks argumented.
    def pivoting(self, from_row, to_row):
        if from_row == to_row:
            return True
        temp_row = self.matrix[to_row].copy()
        self.matrix[to_row] = self.matrix[from_row]
        self.matrix[from_row] = temp_row

    def generate_solution_gauss():
        prin('')

    def generate_solution_gauss_jordan(self):
        print('')
