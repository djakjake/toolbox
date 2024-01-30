# standard imports

# toolbox imports

# Print imports
from . inputs import Default

# =============================================================================
# Print Definition
# =============================================================================

class Print(Default):

    # =========================================================================
    # -------------------------------------------------------------------------

    def __init__(self, *args, **kwargs):
        pass

    # -------------------------------------------------------------------------
    # =========================================================================

    def _print(self, *args, **kwargs):
        pass

    # -------------------------------------------------------------------------

    def __print_item(self, *args, **kwargs):
        pass

    # -------------------------------------------------------------------------

    def __print_list(self, *args, **kwargs):
        pass

    # -------------------------------------------------------------------------

    def __print_dictionary(self, *args, **kwargs):
        pass

    # -------------------------------------------------------------------------

    def __print_data(self, *args, **kwargs):
        pass

    # =========================================================================

    def _generate_indent(self, *args, **kwargs):
        pass

    # =========================================================================

    def _generate_header(self, *args, **kwargs):
        pass

    # =========================================================================

    def _generate_decorator(self, *args, **kwargs):
        pass

    # =========================================================================

    @staticmethod
    def _choose_param(key, *default, **kwargs):
        if key in kwargs:
            return kwargs[key]
        elif len(default) == 1:
            return default[0]
        elif hasattr(Default, key):
            return getattr(Default, key)
        else:
            print(f"
                \nERROR [_choose_param] could not determine value from:\
                \n      key          : {key}\
                \n      default      : {default}\
                \n      kwargs (keys): {kwargs.keys()}\
            ")
            exit()

