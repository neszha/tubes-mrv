import numpy as np
import module.init as init
import module.console as console
from module.OBEClass import OBE

# Object untuk menyelesaikan permasalahan SPL pada matriks hilbert.
# #
class Hilbert:
    ### Constructor method.
    def __init__(self, use):
        self.size = 0
        self.matrix = []
        self.file_log = 'hilbert_activity.txt'
        self.solution_data = {}
        self.solution = []

        self.input_size()
        self.generate_matriks_hilbert()
        self.menu_calculate_method()
        self.save_activity()

    ### Input ukuran matriks hilbert.
    def input_size(self):
        console.clear()
        print('\nHilbert -> Input Ukuran:')
        self.size = int(input('\n(?) Ukuran matriks hilbert (n*n): '))
        self.matrix = np.ones((self.size, self.size + 1))

    ### Menyusun element matriks dengan aturan pada matriks hilbert.
    def generate_matriks_hilbert(self):
        for i in range(self.size):
            for j in range(self.size):
                self.matrix[i][j] = round(1/(i+j+1), 2)

    ### Menu untuk memilih jenis perhitungan yang akan dipakai.
    def menu_calculate_method(self):
        console.clear()
        print('Matriks hilbert dalam matriks argumented:')
        print(self.matrix)
        print('\n[1] Eliminasi Gauss')
        print('[2] Eliminasi Guass Jordan')
        print('[99] Kembali')
        choice = input('\n(?) Hitung menggunakan? ')

        # Kembali ke menu utama.
        if choice == '99': init.main_menu()

        # Menghitung SPL hilbert dengan eliminasi gauss.
        elif choice == '1':
            obe = OBE(self.matrix.copy())
            obe.gauss()
            obe.show_result()
            self.solution = obe.get_solution()
            self.solution_data = obe.solution_data

        # Menghitung SPL hilbert dengan eliminasi gauss jordan.
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

    ### Menyimpan aktifitas perhitungan ke dalam file.
    def save_activity(self):
        path = ['../test/', self.file_log]
        full_path = ''.join(path)
        with open(full_path, 'a') as file:
            file.write(('*' * 70) + '\n')
            file.write('>> Input [n]: ' + str(self.size) + '\n\n')
            file.write('>> Matriks hilbert dalam matriks argumented:\n')
            file.write(str(self.matrix))
            file.write('\n\n>> Hasil: ' + self.solution_data['message'])
            for msg in self.solution_data['data']: file.write('\n' + msg)
            file.write('\n' + ('*' * 70) + '\n')
            file.close()
