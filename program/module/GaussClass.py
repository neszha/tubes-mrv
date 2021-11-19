import module.console as console
import module.init as Route
import module.matrix as matrix

# Object untuk menghanddle operasi guass.
# #
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
        self.matrix = []
        self.matrix = matrix.read_form_console()

    # Membaca inputan data matriks dari file.
    def input_matrix_from_file(self):
        self.matrix = []
        self.matrix = matrix.read_form_file()
        print(self.matrix)

    # Handdle proses perhitungan dengan elimisi guass.
    def spl_core(self):
        print('core')
