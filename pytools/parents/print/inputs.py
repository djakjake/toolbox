# standard imports
import argparse

# pytools imports

# SimUI imports

# =============================================================================
# argument defaults
# =============================================================================

class Default:
    flag_use_tab = False
    indent = 0
    tabwidth = 4

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

parser.add_argument(
    '-use_tab', '--use_tab',
    dest = 'flag_use_tab',
    help = """
    [Print]
    if `True`, will add indentation by `\t`, rather than `" " * `tabwidth`.
    activating negates the `tabwidth` input parameter.
    """
)

parser.add_argument(
    '-indent', '--indent',
    default = Default.indent,
    type = int,
    help = """
    [Print]
    the running counter that tracks the indent level that data will print at.
    the default value specifies the child module's starting indentation level.
    """
)

parser.add_argument(
    '-tabwidth', '--tabwidth',
    default = Default.tabwidth,
    type = int,
    help = """
    [Print]
    when indenting lines, the indentation will be incremented/decremented by
    this amount.
    """
)
