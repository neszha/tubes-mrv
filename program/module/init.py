import module.console as console
from module.SPLClass import SPL
from module.HilbertClass import Hilbert
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
    # choice = '4'

    # Keluar dari console program.
    if choice == '99': console.out()

    # Menggunakan SPLClass untuk menghitung SLP.
    elif choice == '1':
        spl = SPL(True)
        spl.main()

    # Menggunakan HillbertClass untuk memecahkan matriks hilbert.
    elif choice == '2':
        hilbert = Hilbert(True)
        hilbert.main()

    # Menggunakan InterpolasiClass untuk memecahkan matriks polinom interpolasi.
    elif choice == '4': Interpolasi(True)

    # Handdle ketika inputan tidak tersedia.
    else:
        console.selected_unknow()
        main_menu()
