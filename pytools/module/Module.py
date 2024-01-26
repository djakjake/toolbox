# standard imports
import os
import pickle

# toolbox imports

# Module imports

# =============================================================================
# Module Definition
# =============================================================================

class Module:

    def __init__(self, *args, **kwargs):

        # save all key word arguments as attributes
        self.__dict__.update(kwargs)

        # if loading state, do so now
        if self.flag_load_state: self.load_state()

        # make sure the output directory exists
        os.makedirs(self.path_output, exist_ok=True)

        # decide on the tool name
        if self.tool_name is None:
            self.tool_name = self.__class__.__name__

        # decide on the state file path
        self.sate_file = os.path.join(self.path_output, f"{self.tool_name}_state.pkl")

    def save_state(self, *args, **kwargs):

        # choose input parameters
        state_file = self._choose_param('state_file', self.state_file, **kwargs)
        contents = self._choose_param('contents', self.__dict__, **kwargs)

        # store contents into pickle file
        with open(state_file, 'wb') as file:
            pickle.dump(content, file)

    def load_state(self, *args, output=False, **kwargs):

        # choose input parameters
        state_file = self._choose_param('state_file', self.state_file, **kwargs)

        # make sure state file exists
        if not os.path.isfile(state_file):
            return 0

        # read contents of pickle file
        with open(state_file, 'rb') as file:
            contents = pickle.load(file)

        # either return read contents or save them as attributes
        if output:
            return contents
        else:
            self.__dict__.update(contents)

    @staticmethod
    def _choose_param(key, default, **kwargs):
        return kwargs[key] if key in kwargs else default

