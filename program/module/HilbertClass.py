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

        self.input_size()
        self.generate_matriks_hilbert()

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
    def calculate_method_menu(self):
        console.clear()
        print('Persamaan dengan matriks argumented:')
        print(self.matrix)
        print('\n[1] Eliminasi Gauss')
        print('[2] Eliminasi Guass Jordan')
        print('[99] Kembali')
        choice = input('\n(?) Hitung menggunakan? ')

        # Kembali ke menu utama.
        if choice == '99': Route.menu.main_menu()

        # Menghitung SPL hilbert dengan eliminasi gauss.
        elif choice == '1':
            obe = OBE(self.matrix.copy())
            obe.gauss()
            obe.show_result()

        # Menghitung SPL hilbert dengan eliminasi gauss jordan.
        elif choice == '2':
            obe = OBE(self.matrix.copy())
            obe.gauss_jordan()
            obe.show_result()

        # Handdle ketika inputan tidak tersedia.
        else:
            console.selected_unknow()
            self.calculate_method_menu()
