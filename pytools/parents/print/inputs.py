# standard imports
import argparse

# pytools imports

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
    description = 'Print arguments',
    formatter_class = argparse.ArgumentDefaultsHelpFormatter,
    add_help = False,
)

# =============================================================================
# parser arguments
# =============================================================================

#parser.add_argument(
#    help = """
#    [Print]
#    """
#)
