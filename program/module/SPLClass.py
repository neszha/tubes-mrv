import numpy as np
import module.console as console
import module.init as Route

# Object untuk menghanddle operasi guass.
# #
class SPL:
    # Constructor method.
    def __init__(self, use):
        self.use = use
        self.selected_input = 0
        self.selected_method = 0
        self.matrix = []

    # Main method.
    def main(self):
        self.matrix_input_menu()
        self.calculate_method_menu();

    # Menampilkan menu metode input.
    def matrix_input_menu(self):
        console.clear()
        print('\nSPL -> [Metode Input]:')
        print('[1] Input dari Console')
        print('[2] Input dari File')
        print('[99] Kembali')

        self.selected_input = input('\nMetode input? ')
        # self.selected_input = '2'

        # Validasi pilihan metode input.
        if self.selected_input == '99':
            # Kembali ke menu utama.
            Route.menu.menu_spl()

        elif self.selected_input == '1':
            # Input matriks dari layar console.
            self.input_matrix_from_console()

        elif self.selected_input == '2':
            self.input_matrix_from_file()

        else:
            # Handdle ketika inputan tidak tersedia.
            console.selected_unknow()
            self.matrix_input_menu()

    def calculate_method_menu(self):
        console.clear()
        print('Persamaan dengan matriks argumented:')
        print(self.matrix)
        print('\nHitung menggukana?')
        print('[1] Input dari Console')
        print('[2] Input dari File')
        print('[99] Kembali')

    # Input persamaan SLP ke dalam metriks argumented.
    def input_matrix_from_console(self):
        console.clear()
        print('\nSPL -> Input Console:')

        # Melakukan deklarasi persamaan.
        m = int(input('\nJumlah persamaan: '))
        n = int(input('Jumlah variable: '))

        # Input persamaan ke matriks argumented ke `self.matrix`.
        self.matrix = []
        for i in range(m):
            m_row = []
            msg = '[#] Input persamaan ke-{0}'
            print(msg.format(i + 1))
            j_next = 0
            for j in range(n):
                msg = '    X({0},{1}) = '
                m_row.append(int(input(msg.format(i + 1, j + 1))))
                j_next += 1
            msg = '    b({0},{1}) = '
            m_row.append(int(input(msg.format(i + 1, j_next + 1))))
            self.matrix.append(m_row)

        self.matrix = np.array(self.matrix)

    # Membaca inputan data matriks dari file.
    # Path file absolute dari folder '../test/'
    # Default path file => `spl_input.txt`
    def input_matrix_from_file(self):
        path = ['../test/', 'spl_input.txt']
        temp = '\nMasukan nama file (default: {0}): '
        temp_input = str(input(temp.format(path[1])))
        if temp_input != '':
            path[1]= temp_input
        full_path = ''.join(path)
        self.matrix = np.loadtxt(full_path, dtype='i', delimiter=' ')
