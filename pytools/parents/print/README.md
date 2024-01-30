# **print**

This is a python module to allow for specialized printing instructions that can be used and/or inherited by other modules.

# **Description**

# **Requirements**

# **imitations and Assumptions**

# **How-To**

# **Classes**

## **Print**

`Print` is the main class of the `print` module.

### **Inputs**

| parameter | default | units | type |description |
|-----------|---------|-------|------|------------|
| `flag_use_tab` | `False` | `bool` | if `True`, will add indentation by `\t`, rather than `" " * `tabwidth`. activating negates the `tabwidth` input parameter. |
| `indent` | 0 | -- | `int` | the running counter that tracks the indent level that data will print at. the default value specifies the child module's starting indentation level. |
| `tabwidth` | 4 | -- | `int` | when indenting lines, the indentation will be incremented/decremented by this amount. |

### **Outputs**

All output is directed to the terminal out.

### **Methods**

#### **__init__(self, \*args, \*\*kwargs)**

The `Print` constructor. As of right now, no specialized print instructions exist.

#### **_print(self, \*args, \*\*kwargs)**

#### **__print_item(self, \*args, \*\*kwargs)**

#### **__print_list(self, \*args, \*\*kwargs)**

#### **__print_dictionary(self, \*args, \*\*kwargs)**

#### **__print_data(self, \*args, \*\*kwargs)**

#### **_generate_indent(self, \*args, \*\*kwargs)**

#### **_generate_header(self, \*args, \*\*kwargs)**

#### **_generate_decorator(self, \*args, \*\*kwargs)**

#### **_choose_param(key, \*default, \*\*kwargs)**

Looks for specified `key` in `kwargs` dictionary.
- If the `key` does exist, it will fetch and return the item from the `kwargs` dictionary.
- If the `key` does not exist and `default` was provided, will return the `default` value.
- If the `key` does not exist and `default` was not provided, will attempt to fetch and return the 'key` attribute from the locally defined `Default` class.
- If all else fails, perform a hard exit

# **Functions**
