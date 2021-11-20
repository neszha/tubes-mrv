import numpy as np
import module.console as console
import module.init as Route

# Object untuk ...
# #
class Polinom:
    # Constructor method.
    def __init__(self, use):
        self.use = use
        self.selected_input = 0
        self.matrix = []
