import numpy as np
import module.console as console
import module.init as Route

# Object untuk ...
# #
class Electric:
    
    # Constructor method.
    def __init__(self, use):
        self.use = use
        self.selected_input = 0
        self.matrix = []
        self.input_i = 0;
        self.input_v = 0;

    def main(self):
        
        # console.clear()
        self.masukan_nilai_i()
        self.masukan_nilai_v()
        self.tes()
        
    def masukan_nilai_i(self):
        self.input_i = input("Masukan Nilai I: ")
        
    def masukan_nilai_v(self):
        self.input_v = input("Masukan Nilai V: ")
        
    def tes(self):
        print(self.input_i)
        print(self.input_v)