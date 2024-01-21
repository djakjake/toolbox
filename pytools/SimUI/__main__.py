# standard imports

# pytools imports
from pytools.functions import parse_args

# SimUI imports
from inputs import parser
from SimUI import SimUI

# =============================================================================
# run main program
# =============================================================================

if "__main__" == __name__:
    kwargs = parse_args(parser)
    SimUI(**kwargs)
