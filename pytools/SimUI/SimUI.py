# standard imports
import _tkinter

# pytools imports
from pytools.parents.module import Module

# SimUI imports
from GUI import GUI
from inputs import Default

# =============================================================================
# SimUI Definition
# =============================================================================

class SimUI(Default, Module, GUI):

    # =========================================================================
    # -------------------------------------------------------------------------

    def __init__(self, *args, **kwargs):
        Module.__init__(self, *args, **kwargs)
        GUI.__init__(self, *args, **kwargs)

    # -------------------------------------------------------------------------
    # =========================================================================

    def load_input_file(self, *args, **kwargs):
        pass

    # =========================================================================

    def run_executable_program(self, *args, **kwargs):
        pass

    # =========================================================================

