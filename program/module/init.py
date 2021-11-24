import module.console as console
from module.SPLClass import SPL
from module.HilbertClass import Hilbert

### Kontrol menu utama.
def main_menu():
    console.clear()
    print('>>> MENU UTAMA PROGRAM PERHITUNGAN MATRIKS <<<\n')
    print('[1] Sistem Persamaan Linier (SPL)')
    print('[2] Matriks Hilbert')
    print('[3] Rangkaian Listrik')
    print('[4] Polinom Interpolasi')
    print('[99] Keluar')

    choice = input('\n(?) Pilih menu: ')
    # choice = '2'

    # Validasi input pilihan menu.
    if choice == '99': # Keluar dari console program.
        console.out()
    elif choice == '1': # Menggunakan SPLClass untuk menghitung SLP.
        spl = SPL(True)
        spl.main()
    elif choice == '2': # Menggunakan HillbertClass untuk memecahkan matriks hilbert.
        hilbert = Hilbert(True)
        hilbert.main()
    else: # Handdle ketika inputan tidak tersedia.
        console.selected_unknow()
        main_menu()
