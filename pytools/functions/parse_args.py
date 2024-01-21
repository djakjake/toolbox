def parse_args(*args, **kwargs):
    """
    DESCRIPTION:
    takes any number of argument parser objects and/or key word arguments and
    organizes them all into a single dictionary.

    the argument parser objects are parsed first and are parsed in the order
    they are given. the given keywords are added last.

    for any arguments/keys that are received multiple times, priority is given
    to the last one received.

    INPUT:
    *args       argument parser objects
    **kwargs    key word arguments

    OUTPUT:
    dict
    """
    opts = {}
    for parser in args:
        opts_ = parser.parse_args()
        opts.update(opts_)
    opts.update(kwargs)
    return opts
