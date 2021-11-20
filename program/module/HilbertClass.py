import numpy as np
import module.console as console
import module.init as Route
import module.matrix as matrix

# Object untuk ...
# #
class Hilbert:
    # Constructor method.
    def __init__(self, use):
        self.use = use
        self.selected_input = 0
        self.matrix = []
