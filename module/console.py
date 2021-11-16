import os
import time

# Membersihkan tampilan console.
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# Keluar dari program dengan sebuah pesan.
def out():
    print(".\n.\n.")
    print('Anda telah keluar dari program.')
    exit(1)

# Menampilkan pesan dengan delay.
# Default delay 1 detik.
def selected_unknow(delay = 1):
    print('\n<< INPUTAN TIDAK TERSEDIA >>')
    time.sleep(delay)
