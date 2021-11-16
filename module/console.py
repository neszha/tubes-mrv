import os
import time

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def out():
    print(".\n.\n.")
    print('Anda telah keluar dari program.')
    exit(1)

def selected_unknow():
    print('\n<< INPUTAN TIDAK TERSEDIA >>')
    time.sleep(1)
