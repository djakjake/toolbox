# functions

This directory contains an `__init__.py` file that allows aliasing. For example:
```python
from pytools.functions import parse_args
```
as apposed to:
```python
from pytools.functions.parse_args import parse_args
```

## `def parse_args(*args, **kwargs)`

```python
DESCRIPTION:
takes any number of argument parser objects and/or key word arguments and
organizes them all into a single dictionary.

the argument parser objects are parsed first and are parsed in the order
they are given. the given keywords are added last.

for any arguments/keys that are received multiple times, priority is given
to the last one received.

INPUT:
*args       argument parser objects
kwargs    key word arguments

OUTPUT:
dict
```
