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
        self.output_in_file = False
        self.file = {
            'in': 'input.txt',
            'out': 'output.txt',
            'log': 'activity.txt'
        }
        self.solution_data = {}
        self.solution = []

        self.menu_matrix_input()
        self.menu_calculate_method()
        self.save_activity()

    ### Menampilkan menu metode input.
    def menu_matrix_input(self):
        console.clear()
        print('\nSPL -> [Metode Input]:')
        print('[1] Input dari Console')
        print('[2] Input dari File')
        print('[99] Kembali')

        choice = input('\n(?) Metode input? ')

        # Kembali ke menu utama.
        if choice == '99': init.main_menu()
        # Input matriks dari layar console.
        elif choice == '1': self.input_matrix_from_console()
        # Input matriks dari file.
        elif choice == '2': self.input_matrix_from_file()
        # Handdle ketika inputan tidak tersedia.
        else:
            console.selected_unknow()
            self.menu_matrix_input()

    ### Menu untuk memilih jenis perhitungan yang akan dipakai.
    def menu_calculate_method(self):
        console.clear()
        print('Persamaan dengan matriks argumented:')
        print(self.matrix)
        print('\n[1] Eliminasi Gauss')
        print('[2] Eliminasi Guass Jordan')
        print('[99] Kembali')

        choice = input('\n(?) Hitung menggunakan? ')

        # Kembali ke input matrix menu.
        if choice == '99': self.menu_matrix_input()

        # Menghitung SPL dengan eliminasi gauss.
        elif choice == '1':
            obe = OBE(self.matrix.copy())
            obe.gauss()
            obe.show_result()
            self.solution = obe.get_solution()
            self.solution_data = obe.solution_data

        # Menghitung SPL dengan eliminasi gauss jordan.
        elif choice == '2':
            obe = OBE(self.matrix.copy())
            obe.gauss_jordan()
            obe.show_result()
            self.solution = obe.get_solution()
            self.solution_data = obe.solution_data

        # Handdle ketika inputan tidak tersedia.
        else:
            console.selected_unknow()
            self.menu_calculate_method()

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
    ### Path file absolute dari folder '../test/spl/'
    ### Default path file => `input.txt`
    def input_matrix_from_file(self):
        console.clear()
        print('SPL -> Input File:')
        print('\nLokasi file absolute dari folder `../test/spl/`')

        # Menbaca data dari file.
        self.output_in_file = True
        path = ['../test/spl/', self.file['in']]
        temp = 'Masukan nama file (default: {0}): '
        temp_input = str(input(temp.format(path[1])))
        if temp_input != '': path[1]= temp_input
        full_path = ''.join(path)
        self.matrix = np.loadtxt(full_path, dtype = float, delimiter = ' ')

    ### Menyimpan aktifitas perhitungan ke dalam file.
    def save_activity(self):
        # Menambahkan aktifitas ke file.
        path = ['../test/spl/', self.file['log']]
        full_path = ''.join(path)
        with open(full_path, 'a') as file:
            file.write(('*' * 70) + '\n')
            file.write('>> Persamaan dengan matriks argumented:\n')
            file.write(str(self.matrix))
            file.write('\n\n>> Hasil: ' + self.solution_data['message'])
            for msg in self.solution_data['data']: file.write('\n' + msg)
            file.write('\n' + ('*' * 70) + '\n')
            file.close()

        # Menampilkan output di file.
        if self.output_in_file:
            path = ['../test/spl/', self.file['out']]
            full_path = ''.join(path)
            file = open(full_path, 'w')
            file.write('')
            file.close()
            file = open(full_path, 'a')
            for msg in self.solution_data['data']: file.write(msg + '\n')
            file.close()
