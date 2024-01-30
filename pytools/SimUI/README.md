# SimUI

# Description

A graphical user interface that allows the user to:
- load previous settings
- adjust settings
- save settings
- execute specified program with specified settings

# Requirements
- Python 3.6+ | 3.10.12
- tkinter 3.0+ | 8.6

# imitations and Assumptions

# How-To

# Classes

## SimUI(GUI)

### Input

| parameter | default | units | type |description |
|-----------|---------|-------|------|------------|
| `flag_no_gui` | `False` | -- | bool | if `True`, will skip the GUI and will execute all programs via terminal only |
| `flag_load_state` | `False` | -- | bool | if `True`, will load the last saved state |
| `flag_save_state` | `False` | -- | bool | if `True`, will save the state, prior to executing main program |
| `exe_programs` | `None` | -- | [str,] | the main program that will be executed. all inputs will be fed into program |
| `input_files` | `None` | -- | [str,] | the input file(s) that will be parsed and fed into `exe_programs`. |
| `path_output` | current working directory | -- | str | the path were any/all output is directed. |
| `tool_name` | `None` | -- | str | the name of the tool/sim/project. if not provided, will default to the first `exe_programs` item. |

**NOTE:** `exe_programs` & `input_files`
1) **one to one:** for each `exe_programs` there is one `input_files`
1) **many to many:**
   - if the number of `exe_programs` and `input_files` match, it is a **one to one** relationship.
   - if the number of `exe_programs` and `input_files` do not match, raise `RuntimeError`.
1) **one to many:**
   - if there are many `exe_programs` and only one `input_files`, all `exe_programs` will share the same `input_files`.
   - if there are many `input_files` and only one `exe_programs`, the `exe_programs` will receive the input as a dictionary where each `input_files` basename will be the key and the `input_files` contents will be the value.
1) **many|one to None:**
  - if there are many|one `exe_programs` and no `input_files`, all `exe_programs` will be executed w/o input.
  - if there are many|one `input_files` and no `exe_programs`, raise `RuntimeError`
1) **None and None:** raise `RuntimeError`

### Output

File
| basename | destination | description |
|----------|-------------|-------------|
| `<tool_name>_state.pkl` | `<path_output>/<basename>` | the saved state file that will be saved and/or loaded. |

Data
| parameter | units | type | description |
|-----------|-------|------|-------------|

### Methods

#### '__init__(self, *args, **kwargs)'

#### 'load_input_file(self, *args, **kwargs)'

#### 'run_executable_program(self, *args, **kwargs)'

## GUI

### Input

### Output

### Methods

#### '__init__(self, *args, **kwargs)'

#### '_create_frame(self, *args, **kwargs)'

#### '_destroy_frame(self, *args, **kwargs)'

#### '_create_box_select_multiple(self, *args, **kwargs)'

#### '_create_box_select_binary(self, *args, **kwargs)'

#### '_create_box_user_input(self, *args, **kwargs)'
