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

    ### Main method.
    def main(self):
        self.input_size()
        self.generate_matriks_hilbert()
        self.calculate_method_menu()

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
        choice = input('\n(?) Hitung menggukana? ')

        # Validasi pilihan metode eliminasi.
        if choice == '99': # Kembali ke menu utama.
            Route.menu.main_menu()
        elif choice == '1': # Menghitung SPL hilbert dengan eliminasi gauss.
            obe = OBE(self.matrix.copy())
            obe.gauss()
            obe.show_result()
        elif choice == '2': # Menghitung SPL hilbert dengan eliminasi gauss jordan.
            obe = OBE(self.matrix.copy())
            obe.gauss_jordan()
            obe.show_result()
        else: # Handdle ketika inputan tidak tersedia.
            console.selected_unknow()
            self.calculate_method_menu()
