import module.console as console
import module.init as Route

# Object untuk mengelola navigasi menu.
# #
class Menu:
    # Constructor function.
    def __init__(self, use):
        self.use = use
        self.selected_main_menu = 0
        self.selected_menu_1 = 0
        self.selected_menu_2 = 0

    # Kontrol menu utama.
    def main_menu(self):
        console.clear()
        print('>>> MENU UTAMA PROGRAM PERHITUNGAN MATRIKS <<<\n')
        print('Pilih opsi:')
        print('[1] Sistem Persamaan Linier (SPL)')
        print('[2] Menghitung Determinan')
        print('[3] Menentukan Matriks Balikan')
        print('[99] Keluar')

        # self.selected_main_menu = input('Input opsi: ')
        self.selected_main_menu = '1'

        # Validasi input pilihan menu.
        if self.selected_main_menu == '99':
            console.out()
        elif self.selected_main_menu == '1':
            Route.menu.menu_spl()
        else:
            console.selected_unknow()
            Route.menu.main_menu()

    # Kontrol menu pada sub-menu spl.
    def menu_spl(self):
        console.clear()
        print('SPL -> Metode Perhitungan:')
        print('[1] Eliminasi Gauss')
        print('[2] Eliminasi Gauss-Jordan')
        print('[3] Metode Matriks Balikan')
        print('[4] Kaidah Cramer')
        print('[99] Kembali ke Manu Utama')

        # self.selected_menu_1 = input('Pilih Metode: ')
        self.selected_menu_1 = '1'

        # Validasi input pilihan menu.
        if self.selected_menu_1 == '99':
            Route.menu.main_menu()
        elif self.selected_menu_1 == '1':
            Route.gauss.menu()
        else:
            console.selected_unknow()
            Route.menu.menu_spl()
