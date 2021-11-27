import numpy as np
import module.init as init
import module.console as console
from module.OBEClass import OBE

# Object untuk mengelola data titik mengunakan interpolasi polinom.
# #
class Interpolasi:
    ### Constructor method.
    def __init__(self, run):
        self.points = []
        self.matrix = []
        self.output_in_file = False
        self.file = {
            'in': 'input.txt',
            'out': 'output.txt',
            'log': 'activity.txt'
        }
        self.solution = []
        self.test_history = []

        self.menu_input_method()
        self.menu_calculate_method()

    ### Menampilkan menu metode input.
    def menu_input_method(self):
        console.clear()
        print('\nInterpolasi -> [Metode Input]:')
        print('[1] Input dari Console')
        print('[2] Input dari File')
        print('[99] Kembali')

        choice = input('\n(?) Metode input? ')

        # Kembali ke menu utama.
        if choice == '99': init.main_menu()
        # Input data dari layar console.
        elif choice == '1': self.input_points_from_console()
        # Input data dari file.
        elif choice == '2': self.input_points_from_file()
         # Handdle ketika inputan tidak tersedia.
        else:
            console.selected_unknow()
            self.menu_input_method()

    ### Menu untuk memilih jenis perhitungan yang akan dipakai.
    def menu_calculate_method(self):
        console.clear()
        print('Persamaan dengan matriks argumented:')
        print(self.matrix)

        print('\n[1] Eliminasi Gauss')
        print('[2] Eliminasi Guass Jordan')
        print('[99] Kembali')

        choice = input('\n(?) Hitung menggunakan? ')

        # Kembali ke menu interpolasi.
        if choice == '99':
            self.menu_input_method()

        # Menghitung matriks dengan eliminasi gauss.
        elif choice == '1':
            obe = OBE(self.matrix.copy())
            obe.gauss()
            self.solution = obe.get_solution()
            self.solution_data = obe.solution_data
            self.show_solution()
            self.calculate_estimation()

        # Menghitung matriks dengan eliminasi gauss jordan.
        elif choice == '2':
            obe = OBE(self.matrix.copy())
            obe.gauss_jordan()
            self.solution = obe.get_solution()
            self.solution_data = obe.solution_data
            self.show_solution()
            self.calculate_estimation()

        # Handdle ketika inputan tidak tersedia.
        else:
            console.selected_unknow()
            self.menu_calculate_method()

    ### Input nilai titik ke variable `self.points`.
    def input_points_from_console(self):
        console.clear()
        print('\nInterpolasi -> Input Console:')

        # Input persamaan ke matriks argumented ke `self.matrix`.
        n = int(input('\n(?) Jumlah titik data: '))
        self.points = np.ones((n, 2))
        for i in range(n):
            msg = '[#] Input data titik ke-{0}'
            print(msg.format(i + 1))
            msg = '    X({0}) = '
            self.points[i][0] = float(input(msg.format(i + 1)))
            msg = '    Y({0}) = '
            self.points[i][1] = float(input(msg.format(i + 1)))
        self.generate_points_to_matrix_argumented()

    ### Membaca inputan data titik dari file.
    ### Path file absolute dari folder '../test/interpolasi/'
    ### Default path file => `input.txt`
    def input_points_from_file(self):
        console.clear()
        print('Interpolasi -> Input File:')
        print('\nLokasi file absolute dari folder `../test/interpolasi/`')

        # Menbaca data dari file.
        self.output_in_file = True
        path = ['../test/interpolasi/', self.file['in']]
        temp = 'Masukan nama file (default: {0}): '
        temp_input = str(input(temp.format(path[1])))
        if temp_input != '': path[1]= temp_input
        full_path = ''.join(path)
        self.points = np.loadtxt(full_path, dtype = float, delimiter = ' ')
        self.generate_points_to_matrix_argumented()

    ### Membuat matrik argumented interpolasi dari data titik.
    def generate_points_to_matrix_argumented(self):
        console.clear()
        [row, col] = self.points.shape
        self.matrix = np.ones((row, row+1))
        for i in range(row):
            [x, y] = self.points[i]
            for j in range(row): self.matrix[i][j] = pow(x, j)
            self.matrix[i][j+1] = y

    ### Membuat formula persamaan polinomial (string).
    def generate_polynomial_equation_formula(self):
        [row, col] = self.points.shape
        key = 'P'+ str(row-1) +'(X) = '
        temp_array = []

        def to_string(number):
            if(number > 0): return str(number)
            return '('+ str(number) +')'

        for i in range(len(self.solution)):
            if i == 0: temp_array.append(to_string(self.solution[i]))
            else : temp_array.append(
                to_string(self.solution[i]) + '(X^' + str(i) + ')'
            )
        return key + ' + '.join(temp_array)

    ### Menampilkan persamaan polinom yang didapatkan.
    def show_solution(self):
        console.clear()
        print('Persamaan dengan matriks argumented:')
        print(self.matrix)

        print('\nPersamaan polinom:')
        string_formula = self.generate_polynomial_equation_formula()
        print(string_formula)

    ### Menghitung nilai estimasi menggunakan rumus polinomial yang didapatkan.
    def calculate_estimation(self):
        [row, col] = self.points.shape
        print('\nMenghitung estimasi menggunakan P'+ str(row-1) +'(X):')
        print('[X]: [a] Menu Utama, [b] Selesai')

        while True:
            choice = input('\n(?) Masukan nilai X: ')

            # Aksi menu.
            if choice in ['a', 'b']:
                if choice == 'a': init.main_menu()
                elif choice == 'b':
                    self.save_activity()
                    console.out()
                break

            # Melakukan perhitungan dengan rumus polinomial.
            else:
                x = float(choice)
                result = 0
                for i in range(len(self.solution)): result += self.solution[i] * pow(x, i)
                msg = 'P{0}({1}) = {2}'
                parse_msg = msg.format(row-1, x, result)
                self.test_history.append(parse_msg)
                print('Hasil dari ' + parse_msg)

    ### Menyimpan aktifitas perhitungan ke dalam file.
    def save_activity(self):
        string_array = []

        # Menyusun output data ke dalam string.
        string_array.append('>> Persamaan polinomial:')
        string_array.append(self.generate_polynomial_equation_formula())
        string_array.append('\n>> Tes polinomial:')
        for test in self.test_history: string_array.append(test)

        # Meyimpan output program ke file.
        if self.output_in_file:
            path = ['../test/interpolasi/', self.file['out']]
            full_path = ''.join(path)
            with open(full_path, 'w') as file:
                file.write('\n'.join(string_array))
                file.close()

        # Menambahkan aktifitas ke file.
        path = ['../test/interpolasi/', self.file['log']]
        full_path = ''.join(path)
        with open(full_path, 'a') as file:
            file.write(('*' * 70) + '\n')
            file.write('\n'.join(string_array))
            file.write('\n' + ('*' * 70) + '\n')
            file.close()
