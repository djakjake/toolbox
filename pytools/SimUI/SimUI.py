# standard imports
import _tkinter

# pytools imports
from pytools.module import Module

# SimUI imports
from GUI import GUI

# =============================================================================
# SimUI Definition
# =============================================================================

class SimUI(Module, GUI):

    def __init__(self, *args, **kwargs):
        Module.__init__(self, *args, **kwargs)
        GUI.__init__(self, *args, **kwargs)

    def save_state(self, *args, **kwargs):
        pass

    def load_state(self, *args, **kwargs):
        pass

    def load_input_file(self, *args, **kwargs):
        pass

    def run_executable_program(self, *args, **kwargs):
        pass

