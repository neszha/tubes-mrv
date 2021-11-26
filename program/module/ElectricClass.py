import numpy as np
import module.init as init
import module.console as console
from module.OBEClass import OBE

# Object untuk menghitung persamaan pada rangkaian listrik.
# #
class Electric:
    ### Constructor method.
    def __init__(self, use):
        self.matrix = []
        self.solution = []
        self.keys = ['I12', 'I52', 'I32', 'I65', 'I54', 'I43', 'V2', 'V3', 'V4', 'V5']
        self.input = {
            'R12': 5, 'R52': 10, 'R32': 10,
            'R65': 20, 'R54': 15, 'R43': 5,
            'V1': 200, 'V6': 0
        }

        self.setup_matrix_template()
        self.input_value()
        self.calculate()

    ### Melakukan input data yang diketahui.
    def input_value(self):
        console.clear()
        print('\nElectric -> Input:\n')

        # Input data.
        for key in self.input:
            msg = '>> Masukan nilai [{0}]: '
            self.input[key] = float(input(msg.format(key)))

        # Menambahkan isi element dari nilai input `self.input`.
        x = self.matrix
        x[7][0] = self.input['R12']
        x[9][1] = self.input['R52']
        x[4][2] = self.input['R32']
        x[7][3] = self.input['R65']
        x[8][4] = self.input['R54']
        x[5][5] = self.input['R43']
        x[7][10] = self.input['V1']
        x[6][10] = self.input['V6']

    ### Menyaipakan template matrix argumented berddasarkan permasalahan.
    def setup_matrix_template(self):
        # 0:i12, 1:i52, 2:i32, 3:i65, 4:i54, 5:i43, 6:V2, 7:V3, 8:V4, 9:V5, 10:B
        x = self.matrix = np.zeros((len(self.keys), len(self.keys)+1))

        # Template persamaan dari hukum kirchoff.
        x[0][0] = x[0][1] = x[0][2] = x[1][3] = x[2][5] = x[3][4] = 1
        x[1][1] = x[1][4] = x[2][2] = x[3][5] = -1

        # Template persamaan dari hukum ohm.
        x[4][6] = x[5][7] = x[6][9] = x[7][6] = x[8][8] = x[9][6] = 1
        x[4][7] = x[5][8] = x[8][9] = x[9][9] = -1

    ### Mennghitung dan menampilkan solusi persamaan.
    def calculate(self):
        console.clear()
        print('Persamaan dengan matriks argumented:')
        print(self.matrix)

        # Menyelesaikan persamaan dengan eliminasi gauss.
        obe = OBE(self.matrix.copy())
        obe.gauss()
        self.solution = obe.get_solution()

        # Menampilkan solusi.
        print('\nSolusi dari persamaan:')
        i = 0
        for key in self.keys:
            print(' >>', key, ':', self.solution[i])
            i += 1
