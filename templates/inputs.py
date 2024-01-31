# standard imports
import argparse

# toolbox imports
import pytools.parents.module as module

# {tool} imports

# =============================================================================
# argument defaults
# =============================================================================

class Default:
    pass

# =============================================================================
# parser object
# =============================================================================

parser = argparse.ArgumentParser(
    description = '{Tool} arguments',
    formatter_class = argparse.ArgumentDefaultsHelpFormatter,
    parents = [module.parser],
)

# =============================================================================
# parser arguments
# =============================================================================

#parser.add_argument(
#    help = """
#    [{Tool}]
#    """
#)
