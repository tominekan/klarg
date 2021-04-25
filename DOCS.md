# Klarg docs

This is where the documentation and references are.

## Overview
[Introduction](#Introduction)

[Terminology](#Terminology)

[Contributing](#Contributing)

[API Reference](#api-reference)


## Introduction
Klarg is a small and simple command line argument parsing library built with no 3rd party dependencies.


## Terminology
There are a number of terminologies used in this documentation. A command line **switch** or **flag** is a term used to describe an option passed to the arguments of a program, examples include `-l`, or `--klarg-rocks`. These terms will be used interchangeably.

Each function in the API docs has the function name, and then in parenthesis, it's arguments, and after "->", it's return value.
Below the defintion is each argument, it's type, and whether it is mandatory or not.

## Contributing
Check [CONTRIBUTING.md](CONTRIBUTING.md)


## API Reference
This is a list of all the methods, what they do, their arguments, and how they use them.

#### `CONFIG`
`CONFIG` is a dictionary that contains the default configurations, to change it, all you need to do is to set the pick the value you want to change, and only change that value. **Never** try this:

```py
import klarg
klarg.CONFIG = {
    "some_setting": "some_value"
}
```

Doing this will erase all other settings except `"some_setting"`. Instead, do this

```py
import klarg
klarg.config["some_setting"] = "some_value"
```

This makes sure not to change the code and instead changes a particular value. Available settings are

Name                 | Type    | Default Value         | Explanation                                                        |
---------------------|---------|-----------------------|--------------------------------------------------------------------|
`"needs_short_flags"`| `bool`  | `False`               | Controls whether klarg raises an error if a short flag is missing. |
`"long_prefix"`      | `str`   | `"--"`                | Sets what klarg looks for in a multi letter switch.                |
`"short_prefix"`     | `str`   | `"-"`                 | Sets what klarg looks for in a shortened switch                    |
`"help_flag"`        | `tuple` | `("--help", "-h")`    | Sets what klarg looks for to trigger the `on_help` function        |
`"version_flag"`     | `tuple` | `("--version", "-v")` | Sets what klarg looks for to print the `project_version` message   |


### `exists(name) -> bool`
`name: str: NEEDED`

Checks if the `name` exists in the list of command line arguments given, this was designed to be an internal function for making things more readable, but then I realized that it could potentially be helpful.

Example:
```py
# docs_example.py
import klarg

something_exists = klarg.exists("something")
if something_exists:
    print("Something exists")
else:
    print("Nothing exists (that's kind of dark)")

# python docs_example.py does something exist
# Something exists

# python docs_example.py does nothing exist
# Nothing exists (that's kind of dark)
```


#### `get_all() -> list`
Collects all the arguments passed and returns them all as a list full of strings. This is useful when a program needs to collect a list of all the arguments passed on to operate on, it passes everything single option passed to the file.

Example:
```py
# docs_example.py
import klarg

all_args = klarg.get_all()
print(f"All args {all_args}")

# python docs_example.py -a -b "c" -d --efgh --ijklmn 0
# All args ["-a", "-b", "c", "-d", "--efgh", "--ijklmn", "0"]
```

#### `get_bool(name, short) -> bool`
`name: str: NEEDED`

`short: str: optional`

`get_bool` is a function that collects `name`, a string, and `short`, also a string. `name` is the long name for the command line argument, i.e. (`--long-name`). `short` is the shorter name for the command line argument (`-s`). Normally, if `short` is not given, then it will not raise an error, unless `"needs_short_flags"` is set to `True` in `CONFIG`.

Example:
```py
# docs_example.py
import klarg

is_there = klarg.bool("--is-there", "-i")

if (is_there):
    print("Is there")
else:
    print("Is not there")

# python docs_example.py 
# Is not there

# python docs_example.py --is-there
# is there
```

#### `get_str(name, short, on_error) -> str`
`name: str: NEEDED`

`short: str: optional`

`on_error: function: optional`

`get_str` is a function that collects a `name`, which is the multi letter flag, a `short`, which is the shortened version of the flag. There is only one type of errors it can encounter, which is when no value is provided. Because of this, `on_error` is not a dictionary, but a special function that handles when no value is provided.

Example:
```py
# docs_example.py
import klarg
def handle_error_none():
    print(f"No values provided")

some_str = klarg.get_str("--some-str", "-s", on_error=handle_error_none)

print(f"{some_str} is cool")

# python docs_example.py --some-str
# No values provided

# python docs_example.py -s "klarg"
# klarg is cool
```

#### `get_num(name, short, on_error) -> num*`
`name: str: NEEDED`

`short: str: optional`

`on_error: dict: optional`

`get_num` is a function that collects a `name`, which is the multi letter flag, a `short`, which is the shortened version of the flag. There are two possible types of errors it can encounter, one being that the value it got was not a number, it did not get a value at all, or that there are multiple declarations of that flag. The error names are `ERR_NUM`, `ERR_NONE` and `ERR_MUL` respectively. `on_error` is a dictionary, all three keys, `ERR_NUM`,`ERR_NONE` and `ERR_MUL` are not all needed, because there is default handling for those types of errors. The default handling for these errors return exit code 1. However, if there is no flag with the name of `name`, then `get_num` returns None.

\* num can be either an integer or a floating point integer.

Example:
```py
# docs_example.py
import klarg
def handle_error_num(value):
    print(f"{value} is not a number")

def handle_error_none():
    print("No values provided")

error_handlers = {
    "ERR_NUM": handle_error_num(),
    "ERR_NONE": handle_error_none()
}

number_something = klarg.get_num(name="--number-something", short="-n", on_error=error_handlers)
print(f"The suprise number is {number_something}")

# python docs_example.py -n 1a
# 1a is not a number

# python docs_example.py -n 
# No values provided

# python docs_example.py -n 12345
# The suprise number is 12345
```

#### `on_help(action) -> None`
`action: function: NEEDED`

The `action` is run when klarg detects the help flag. What klarg looks for can be configured in `CONFIG` with the option `"help_flag"`.

Example:
```py
# docs_example.py
import klarg
def display_help_message():
    print("Here you go")

klarg.on_help(display_help_message)

# python docs_example.py --help
# Here you go
```

#### `project_version(message) -> None`
`message: str: NEEDED`

Klarg displays the `message` when the version flag is detected. What klarg looks for can be configured in `CONFIG` with the option `"version_flag"`.

Example:
```py
# docs_example.py
import klarg
klarg.project_version("This project version is 1.2.3")

# python docs_example.py --version
# This project version is 1.2.3
```


#### `command(command_name)`
`name: str: NEEDED`

This creates a class with the command line that has the functions `project_version()`, `on_help()`, `get_num()`, `get_str()`, `get_bool()`, and `get_all()`. The only difference is that the arguments are parsed after the declaration of the command. This means that if you have a list of command line arguments `["-f", "reply", "-n", "12", "example.txt"]`, and the command name is `reply`. The available Command arguments are `["-n", "12", "example.txt"]`