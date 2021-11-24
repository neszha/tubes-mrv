import module.console as console
import module.init as Route
from module.SPLClass import SPL
from module.HilbertClass import Hilbert

# Object untuk mengelola navigasi menu.
# #
class Menu:
    # Constructor function.
    def __init__(this, use):
        this.selected_main_menu = 0
        this.selected_menu_1 = 0
        this.selected_menu_2 = 0

    # Kontrol menu utama.
    def main_menu(this):
        console.clear()
        print('>>> MENU UTAMA PROGRAM PERHITUNGAN MATRIKS <<<\n')
        print('[1] Sistem Persamaan Linier (SPL)')
        print('[2] Matriks Hilbert')
        print('[3] Rangkaian Listrik')
        print('[4] Polinom Interpolasi')
        print('[99] Keluar')

        this.selected_main_menu = input('\n(?) Pilih menu: ')
        # this.selected_main_menu = '2'

        # Validasi input pilihan menu.
        if this.selected_main_menu == '99': # Keluar dari console program.
            console.out()
        elif this.selected_main_menu == '1': # Menggunakan SPLClass untuk menghitung SLP.
            spl = SPL(True)
            spl.main()
        elif this.selected_main_menu == '2': # Menggunakan HillbertClass untuk memecahkan matriks hilbert.
            hilbert = Hilbert(True)
            hilbert.main()
        else: # Handdle ketika inputan tidak tersedia.
            console.selected_unknow()
            Route.menu.main_menu()

    # Kontrol menu pada sub-menu spl.
    # def menu_spl(this):
    #     console.clear()
    #     print('SPL -> Metode Perhitungan:')
    #     print('[1] Eliminasi Gauss')
    #     print('[2] Eliminasi Gauss-Jordan')
    #     print('[99] Kembali ke Manu Utama')
    #
    #     this.selected_menu_1 = input('\n(?) Pilih metode: ')
    #     # this.selected_menu_1 = '1'
    #
    #     # Validasi input pilihan menu.
    #     if this.selected_menu_1 == '99': Route.menu.main_menu()
    #     elif this.selected_menu_1 == '1': Route.gauss.menu()
    #     else:
    #         console.selected_unknow()
    #         Route.menu.menu_spl()
