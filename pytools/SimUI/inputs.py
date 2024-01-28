# standard imports
import argparse

# pytools imports
import pytools.parents.module as module

# SimUI imports

# =============================================================================
# argument defaults
# =============================================================================

class Default:
    exe_programs = None
    input_files = None

# =============================================================================
# parser object
# =============================================================================

parser = argparse.ArgumentParser(
    description = 'SimUI arguments',
    formatter_class = argparse.ArgumentDefaultsHelpFormatter,
    parents = [module.parser],
)

# =============================================================================
# parser arguments
# =============================================================================

parser.add_argument(
    '--exe_programs',
    nargs = '*',
    default = Default.exe_programs,
    help = """
    [SimUI]
    the main program that will be executed. all inputs will be fed into
    program.
    """
)

parser.add_argument(
    '--input_files',
    nargs = '*',
    default = Default.input_files,
    help = """
    [SimUI]
    the input file(s) that will be parsed and fed into `exe_programs`.
    """
)
