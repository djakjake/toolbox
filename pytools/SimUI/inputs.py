# standard imports
import argparse
import os

# pytools imports

# SimUI imports

# =============================================================================
# argument defaults
# =============================================================================

class Default:
    flag_no_gui = False
    flag_load_state = False
    flag_save_state = False
    exe_programs = None
    input_files = None
    path_output = os.getcwd()
    tool_name = None

# =============================================================================
# parser object
# =============================================================================

parser = argparse.ArgumentParser(
    description = 'SimUI arguments',
    formatter_class = argparse.ArgumentDefaultsHelpFormatter,
)

# =============================================================================
# parser arguments
# =============================================================================

parser.add_argument(
    '-ngui', '--no_gui',
    dest = 'flag_no_gui',
    help = """
    [SimUI]
    if `True`, will skip the GUI and will execute all programs via terminal
    only.
    """
)

parser.add_argument(
    '-ls', '--load_state',
    dest = 'flag_load_state',
    action = 'store_true',
    help = """
    [SimUI]
    if `True`, will load the last saved state.
    """
)

parser.add_argument(
    '-ss', '--save_state',
    dest = 'flag_save_state',
    action = 'store_true',
    help = """
    [SimUI]
    if `True`, will save the state, prior to executing main program.
    """
)

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

parser.add_argument(
    '--path_output',
    default = Default.path_output,
    help = """
    [SimUI]
    the path were any/all output is directed.
    """
)

parser.add_argument(
    '--tool_name',
    default = Default.tool_name,
    help = """
    [SimUI]
    the name of the tool/sim/project. if not provided, will default to the
    first `exe_programs` item.
    """
)

