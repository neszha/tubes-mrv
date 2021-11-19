import numpy as np

# Membaca inputan dari layar console.
def read_form_console():
    # Melakukan deklarasi persamaan.
    m = int(input('\nJumlah persamaan: '))
    n = int(input('Jumlah variable: '))
    # Input nilai matrix ke `matrix`
    matrix = []
    for i in range(m):
        temp = []
        msg = '[#] Input persamaan ke-{0}'
        print(msg.format(i + 1))
        for j in range(n):
            msg = '    X({0},{1}) = '
            temp.append(int(input(msg.format(i + 1, j + 1))))
        matrix.append(temp)
    return matrix

# Membaca inputan data matriks dari file.
# Path file absolute dari folder '../test/'
# Default path file => `slp_input.txt`
def read_form_file():
    path = ['../test/', 'slp_input.txt']
    temp = '\nMasukan nama file (default: {0}): '
    temp_input = str(input(temp.format(path[1])))
    if temp_input != '':
        path[1]= temp_input
    full_path = ''.join(path)
    matrix = np.loadtxt(full_path, dtype='i', delimiter=' ')
    return matrix
