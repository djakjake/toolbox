# standard imports
import os
import pickle

# toolbox imports
from pytools.parents.print import Print

# Module imports
from . inputs import Default

# =============================================================================
# Module Definition
# =============================================================================

class Module(Default, Print):

    # =========================================================================
    # -------------------------------------------------------------------------

    def __init__(self, *args, **kwargs):

        # save all key word arguments as attributes
        self.__dict__.update(kwargs)

        # decide on the tool name
        if self.tool_name is None:
            self.tool_name = self.__class__.__name__

        # deside on path to state_file
        if self.state_file is None:
            self.sate_file = os.path.join(self.path_output, f"{self.tool_name}_state.pkl")

        # if loading state, do so now
        if self.flag_load_state: self.load_state()

        # make sure the output directory exists
        os.makedirs(self.path_output, exist_ok=True)

        # print the current attributes to terminal out
        self._print("starting attributes:", self.__dict__)

    # -------------------------------------------------------------------------
    # =========================================================================

    def save_state(self, *args, **kwargs):

        # choose input parameters
        state_file = self._choose_param('state_file', self.state_file, **kwargs)
        contents = self._choose_param('contents', self.__dict__, **kwargs)

        # store contents into pickle file
        with open(state_file, 'wb') as file:
            pickle.dump(content, file)

    # =========================================================================

    def load_state(self, *args, output=False, **kwargs):

        # choose input parameters
        state_file = self._choose_param('state_file', self.state_file, **kwargs)

        # make sure state file exists
        if not os.path.isfile(state_file):
            self._error(f"the selected state file does not exist!")

        # read contents of pickle file
        with open(state_file, 'rb') as file:
            contents = pickle.load(file)

        # either return read contents or save them as attributes
        if output:
            return contents
        else:
            self.__dict__.update(contents)

    # =========================================================================

