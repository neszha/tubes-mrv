import numpy as np
import module.console as console
import module.init as Route

# Object untuk menghanddle operasi guass.
# #
class OBE:
    # Constructor method.
    def __init__(self, use):
        self.use = use
        self.selected_input = 0
        self.matrix = []

    def gauss(self):
        print('gauss')

    def gauss_jordan(self):
        print('gauss_jordan')
