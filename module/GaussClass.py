import module.console as console
import module.init as Route

class Gauss:
    # Constructor function.
    def __init__(self, use):
        self.use = use
        self.selected_input = 0
        self.matrix = []

    # Kontrol menu pada perhitungan dengan metode gauss.
    def menu(self):
        console.clear()
        print('\nSPL -> Gauss -> Metode Input:')
        print('[1] Input dari Console')
        print('[2] Input dari File')
        print('[99] Kembali')

        # self.selected_input = input('Masukan Pilihan: ')
        self.selected_input = '1'

        if self.selected_input == '99':
            Route.menu.menu_spl()
        elif self.selected_input == '1':
            self.input_matrix_from_console()
        elif self.selected_input == '2':
            self.input_matrix_from_file()
        else:
            self.selected_unknow()

    # Membaca inputan dari layar console.
    def input_matrix_from_console(self):
        print('')

        # Melakukan deklarasi persamaan.
        m = int(input('Jumlah persamaan: '))
        n = int(input('Jumlah variable: '))

        # Input nilai matrix ke `self.matrix`
        self.matrix = []
        for i in range(m):
            temp = []
            msg = '[#] Input persamaan ke-{0}'
            print(msg.format(i + 1))

            for j in range(n):
                msg = '    X({0},{1}) = '
                temp.append(int(input(msg.format(i + 1, j + 1))))

            self.matrix.append(temp)

        print(self.matrix)

    # Membaca inputan data matriks dari file.
    # Default file => ``
    def input_matrix_from_file(self):
        print('from file')

    # Handdle proses perhitungan dengan elimisi guass.
    def spl_core(self):
        print('core')
