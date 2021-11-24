import numpy as np
import module.console as console
import module.init as Route
from tabulate import tabulate

# Object untuk ...
# #
class Hilbert:
    # Constructor method.
    def __init__(self, use):
        self.use = use
        self.input_n = 0
        self.matrix = []
        self.matrix_augmented = []
        
    # Main method.
    def main(self):
        console.clear()
        self.masukan_nilai_n()
        self.convert_ke_MatrixHilbert()
        self.convert_ke_MatrixAugmented()
        self.pilih_MetodeGauss_dan_lempar_data()

    def masukan_nilai_n(self):
        self.input_n = int(input('Masukan Nilai N: '))
        print()
        
    def convert_ke_MatrixHilbert(self):
        for i in range(self.input_n):
            self.matrix.append([])
            for j in range(self.input_n):
                a = round(1/(i+j+1), 2)
                self.matrix[i].append(a)

        print("Matriks Biasa: ")
        print(tabulate(self.matrix, tablefmt='fancy_grid'))
        print()
        
    def convert_ke_MatrixAugmented(self):
        
        self.matrix_augmented = self.matrix
        
        for i in range(self.input_n):
            self.matrix_augmented[i].append(1)
            
        print("Matriks Augmented: ")
        print(tabulate(self.matrix_augmented, tablefmt='fancy_grid'))
        print()
        
    def pilih_MetodeGauss_dan_lempar_data(self):
        
        print("1. Gaus")
        print("2. Gaus Jordan")
        pilihan = input("Pilih Metode (1/2): ")
        
        if pilihan == '1':
            print('ke gaus')
        elif pilihan == '2':
            print('ke gaus jordan')