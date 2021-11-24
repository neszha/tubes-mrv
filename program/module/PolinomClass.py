import numpy as np
import module.init as init
import module.console as console

# Object untuk ...
# #
class Polinom:
    # Constructor method.
    def __init__(self, use):
        self.use = use
        self.selected_input = 0
        self.matrix = []
