import os

class Menu:
    def __init__(self, use):
        self.use = use
        self.selected_main_menu = 0
        self.selected_menu_1 = 0
        self.selected_menu_2 = 0

    def main_menu(self):
        self.clear()
        print('>>> MENU UTAMA PROGRAM PERHITUNGAN MATRIKS <<<\n')
        print('Pilih opsi:')
        print('[1] Sistem Persamaan Linier (SPL)')
        print('[2] Menghitung Determinan')
        print('[3] Menentukan Matriks Balikan')
        print('[0] Keluar')

        self.selected_main_menu = int(input('Input opsi: '))
        # self.selected_main_menu = 1
        print('')

        # Validasi input pilihan menu.
        if self.selected_main_menu == 0:
            self.exit()
        elif self.selected_main_menu == 1:
            self.menu_1()

    def menu_1(self):
        print('Pilih Metode Perhitungan:')
        print('[1] Eliminasi Gauss')
        print('[2] Eliminasi Gauss-Jordan')
        print('[3] Metode Matriks Balikan')
        print('[4] Kaidah Cramer')
        print('[0] Kembali ke Manu Utama')

        self.selected_menu_1 = int(input('Pilih Metode: '))

        # Validasi input pilihan menu.
        if self.selected_menu_1 == 0:
            self.main_menu()

    def clear(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def exit(self):
        print(".\n.\n.")
        print('Anda telah keluar dari program.')
        exit(1)
