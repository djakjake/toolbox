# standard imports
import argparse

# pytools imports
import pytools.module as module

# SimUI imports

# =============================================================================
# argument defaults
# =============================================================================

class Default:
    pass

# =============================================================================
# parser object
# =============================================================================

parser = argparse.ArgumentParser(
    description = '{tool} arguments',
    formatter_class = argparse.ArgumentDefaultsHelpFormatter,
    parents = [module.parser],
)

# =============================================================================
# parser arguments
# =============================================================================

#parser.add_argument(
#    help = """
#    [{tool}]
#    """
#)