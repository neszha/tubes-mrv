import module.console as console
from module.SPLClass import SPL
from module.HilbertClass import Hilbert
from module.ElectricClass import Electric
from module.InterpolasiClass import Interpolasi

### Kontrol menu utama.
def main_menu():
    console.clear()
    print('>>> MENU UTAMA PROGRAM PERHITUNGAN MATRIKS <<<\n')
    print('[1] Sistem Persamaan Linier (SPL)')
    print('[2] Matriks Hilbert')
    print('[3] Rangkaian Listrik')
    print('[4] Interpolasi')
    print('[99] Keluar')

    choice = input('\n(?) Pilih menu: ')
    # choice = '1'

    # Keluar dari console program.
    if choice == '99': console.out()

    # Menggunakan SPLClass untuk menghitung SLP.
    elif choice == '1': SPL(True)

    # Menggunakan HillbertClass untuk memecahkan matriks hilbert.
    elif choice == '2': Hilbert(True)

    # Menggunakan ElectricClass untuk memecahkan persoalan rangkaian listrik.
    elif choice == '3': Electric(True)

    # Menggunakan InterpolasiClass untuk memecahkan matriks polinom interpolasi.
    elif choice == '4': Interpolasi(True)

    # Handdle ketika inputan tidak tersedia.
    else:
        console.selected_unknow()
        main_menu()
