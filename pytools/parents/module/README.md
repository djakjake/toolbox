# module

# Description

# Requirements

# imitations and Assumptions

# How-To

# Classes

## module

### Inputs

| parameter | default | units | type |description |
|-----------|---------|-------|------|------------|
| `flag_no_gui` | `False` | -- | `bool` | if `True`, will skip the GUI and will execute all programs via terminal only. |
| `flag_load_state` | `False` | -- | `bool` | if `True`, will load the last saved state. |
| `flag_save_state` | `False` | -- | `bool` | if `True`, will save the state, prior to executing main program. |
| `path_output` | `os.getcwd()` | -- | `str` | the path were any/all output is directed. |
| `state_file` | `None` | -- | `str` | the path to the previous saved state file. |
| `tool_name` | `None` | -- | `str` | the name of the tool/sim/project. if not provided, will default to the first `exe_programs` item. |

### Outputs

File
|--------------------------------------|
| basename | destination | description |
|----------|-------------|-------------|

Data
|----------------------------------------|
| parameter | units | type | description |
|-----------|-------|------|-------------|

### Methods

#### `__init__(self, *args, **kwargs)`

The constructor for the `Module` class. Its main purpose is to set initial attributes through a combination of:
- run-time user options
- received key-word arguments
- loading previous state attributes

#### `save_state(self, *args, **kwargs)`

Input:
'state_file = self.state_file`
`contents = self.__dict__`

1) chooses which file and what contents to save
1) saves contents to `.pkl` file.

#### `load_state(self, *args, output=False, **kwargs)`

Input:
'state_file = self.state_file`
`output = False`

If the selected state file exists, an `ERROR` is printed and the program ends; otherwise, the contents are loaded and are either output or saved as attributes.

#### `_choose_param(key, *default, **kwargs)`

Looks for specified `key` in `kwargs` dictionary.
- If the `key` does exist, it will fetch and return the item from the `kwargs` dictionary.
- If the `key` does not exist and `default` was provided, will return the `default` value.
- If the `key` does not exist and `default` was not provided, will attempt to fetch and return the 'key` attribute from the locally defined `Default` class.
- If all else fails, perform a hard exit

#### `_error(self, *msgs, **kwargs)`

Input:
*msgs

Prints an error message of the form:
```bash
ERROR [<function name>]
      msg[0]
      msg[1]
      ...
      msg[N]
```
then exits the program.

# Functions
