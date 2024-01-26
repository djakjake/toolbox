# toolbox - Description

A collection of tools, scripts, functions, files, etc... that can be used for projects.

# bash

## setEnv.sh $1

- must receive valid directory as `$1`
- Creates a new python virtual environment at `$1/vEnv`.
- Activates `$1/vEnv`
- if a `requirements.txt` file exists in `$1`, installs requirements.

# cpp

# pytools

## functions

### parse_args(*args, **kwargs):

```python
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
```

## scripts

## SimUI

# templates

A collection of template files

# tools

A collection of general tools
