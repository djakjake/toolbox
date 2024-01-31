# standard imports
import argparse
import os

# toolbox imports
import pytools.parents.print as _print

# module imports

# =============================================================================
# argument defaults
# =============================================================================

class Default:
    flag_no_gui = False
    flag_load_state = False
    flag_save_state = False
    path_output = os.getcwd()
    state_file = None
    tool_name = None

# =============================================================================
# parser object
# =============================================================================

parser = argparse.ArgumentParser(
    description = 'Module arguments',
    formatter_class = argparse.ArgumentDefaultsHelpFormatter,
    add_help = False,
    parents = [_print.parser],
)

# =============================================================================
# parser arguments
# =============================================================================

parser.add_argument(
    '-ngui', '--no_gui',
    dest = 'flag_no_gui',
    help = """
    [Module]
    if `True`, will skip the GUI and will execute all programs via terminal
    only.
    """
)

parser.add_argument(
    '-ls', '--load_state',
    dest = 'flag_load_state',
    action = 'store_true',
    help = """
    [Module]
    if `True`, will load the last saved state.
    """
)

parser.add_argument(
    '-ss', '--save_state',
    dest = 'flag_save_state',
    action = 'store_true',
    help = """
    [Module]
    if `True`, will save the state, prior to executing main program.
    """
)

parser.add_argument(
    '--path_output',
    default = Default.path_output,
    help = """
    [Module]
    the path were any/all output is directed.
    """
)

parser.add_argument(
    '--state_file',
    default = Default.state_file,
    help = """
    [Module]
    the path to the previous saved state file.
    """
)

parser.add_argument(
    '--tool_name',
    default = Default.tool_name,
    help = """
    [Module]
    the name of the tool/sim/project. if not provided, will default to the
    first `exe_programs` item.
    """
)
