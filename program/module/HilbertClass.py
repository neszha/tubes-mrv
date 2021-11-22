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
        
    # Main method.
    def main(self):
        self.masukan_nilai_n()
        self.convert_ke_hilbert()

    def masukan_nilai_n(self):
        console.clear()
        self.input_n = int(input('Masukan Nilai N: '))
        
    def convert_ke_hilbert(self):
        for i in range(self.input_n):
            self.matrix.append([])
            for j in range(self.input_n):
                a = round(1/(i+j+1), 2)
                self.matrix[i].append(a)

        print(tabulate(self.matrix, tablefmt='fancy_grid'))
        # for i in range(self.input_n):

        #     for j in range(self.input_n):
        #         print(self.matrix[i][j], end=" ")

                
        #     print()
        # print()