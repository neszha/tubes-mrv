import numpy as np
import module.init as init
import module.console as console
import module.matrix as matrix

# Object untuk ...
# #
class Electric:
    # Constructor method.
    def __init__(self, use):
        self.use = use
        self.selected_input = 0
        self.matrix = []
