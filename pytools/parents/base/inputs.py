# standard imports
import argparse

# toolbox imports

# base imports

# =============================================================================
# argument defaults
# =============================================================================

class Default:
    pass

# =============================================================================
# parser object
# =============================================================================

parser = argparse.ArgumentParser(
    description = 'Base arguments',
    formatter_class = argparse.ArgumentDefaultsHelpFormatter,
    add_help = False,
)

# =============================================================================
# parser arguments
# =============================================================================

#parser.add_argument(
#    help = """
#    [Base]
#    """
#)
