import numpy as np
import module.init as init
import module.console as console
from module.OBEClass import OBE

# Object untuk menyelesaikan permasalahan SPL.
# #
class SPL:
    ### Constructor method.
    def __init__(self, use):
        self.matrix = []

    ### Main method.
    def main(self):
        self.matrix_input_menu()
        self.calculate_method_menu();

    ### Menampilkan menu metode input.
    def matrix_input_menu(self):
        console.clear()
        print('\nSPL -> [Metode Input]:')
        print('[1] Input dari Console')
        print('[2] Input dari File')
        print('[99] Kembali')

        choice = input('\n(?) Metode input? ')
        # choice = '2'

        # Validasi pilihan metode input.
        if choice == '99':
            init.main_menu() # Kembali ke menu utama.
        elif choice == '1':
            self.input_matrix_from_console() # Input matriks dari layar console.
        elif choice == '2':
            self.input_matrix_from_file() # Input matriks dari file.
        else: # Handdle ketika inputan tidak tersedia.
            console.selected_unknow()
            self.matrix_input_menu()

    ### Menu untuk memilih jenis perhitungan yang akan dipakai.
    def calculate_method_menu(self):
        console.clear()
        print('Persamaan dengan matriks argumented:')
        print(self.matrix)

        print('\n[1] Eliminasi Gauss')
        print('[2] Eliminasi Guass Jordan')
        print('[99] Kembali')

        choice = input('\n(?) Hitung menggunakan? ')
        # choice = '1'

        # Validasi pilihan metode eliminasi.
        if choice == '99': # Kembali ke input matrix menu.
            self.matrix_input_menu()
        elif choice == '1': # Menghitung SPL dengan eliminasi gauss.
            obe = OBE(self.matrix.copy())
            obe.gauss()
            obe.show_result()
        elif choice == '2': # Menghitung SPL dengan eliminasi gauss jordan.
            obe = OBE(self.matrix.copy())
            obe.gauss_jordan()
            obe.show_result()
        else: # Handdle ketika inputan tidak tersedia.
            console.selected_unknow()
            self.calculate_method_menu()

    ### Input persamaan SLP ke dalam metriks argumented.
    def input_matrix_from_console(self):
        console.clear()
        print('\nSPL -> Input Console:')

        # Input persamaan ke matriks argumented ke `self.matrix`.
        m = int(input('\n(?) Jumlah persamaan: '))
        n = int(input('(?) Jumlah variable: '))
        self.matrix = []
        for i in range(m):
            m_row = []
            msg = '[#] Input persamaan ke-{0}'
            print(msg.format(i + 1))
            j_next = 0
            for j in range(n):
                msg = '    X({0},{1}) = '
                m_row.append(float(input(msg.format(i + 1, j + 1))))
                j_next += 1
            msg = '    B({0},{1}) = '
            m_row.append(float(input(msg.format(i + 1, j_next + 1))))
            self.matrix.append(m_row)

        self.matrix = np.array(self.matrix, dtype = float)

    ### Membaca inputan data matriks dari file.
    ### Path file absolute dari folder '../test/'
    ### Default path file => `spl_input.txt`
    def input_matrix_from_file(self):
        console.clear()
        print('SPL -> Input File:')
        print('\nLokasi file absolute dari folder `../test/`')

        path = ['../test/', 'spl_input.txt']
        temp = 'Masukan nama file (default: {0}): '
        temp_input = str(input(temp.format(path[1])))
        if temp_input != '': path[1]= temp_input
        full_path = ''.join(path)
        self.matrix = np.loadtxt(full_path, dtype = float, delimiter = ' ')
