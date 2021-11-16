import module.console as console
import module.init as Route

class GaussJordan:
    def __init__(self, use):
        self.use = use
        self.selected_input = 0
        self.matrix = []

    def menu(self):
        console.clear()
        print('\nSPL -> Gauss Jordan -> Metode Input:')
        print('[1] Input dari Console')
        print('[2] Input dari File')
        print('[99] Kembali')

        self.selected_input = input('Masukan Pilihan: ')

        if self.selected_input == '99':
            Route.menu.menu_spl()
        elif self.selected_input == '1':
            self.matrix_from_console()
        elif self.selected_input == '2':
            self.matrix_from_file()
        else:
            self.selected_unknow()


    def matrix_from_console(self):
        print('from Console')

    def matrix_from_file(self):
        print('from file')

    def spl_core(self):
        print('core')
