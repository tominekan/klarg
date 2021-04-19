# Klarg docs

This is where the documentation and references are.

## Overview
[Introduction](#Introduction)

[Terminology](#Terminology)

[Contributing](#Contributing)

[API Reference](#API)


## Introduction
Klarg is a small, fast (as python goes 😃) and simple command line argument parsing library built with no 3rd party dependencies.


## Terminology
There are a number of terminologies used in this documentation. A command line **switch** or **flag** is a term used to describe an option passed to the arguments of a program, examples include `-l`, or `--klarg-rocks`. These terms will be used interchangeably.

Each function in the API docs has the function name, and then in parenthesis, it's arguments, and after "->", it's return value.
Below the defintion is each argument, it's type, and whether it is mandatory or not.

## Contributing
Check [CONTRIBUTING.md](CONTRIBUTING.md)


## API Reference
This is a list of all the methods, what they do, their arguments, and how they use them.
NOTE: anything in curly brackets "{" "}" is a variable.


#### `configure(configuration) -> None`
Configure takes in a dictionary called `confguration`

Below is a list of values that configure takes:

`has_short_flags: bool` -- Default: `False` This controls if klarg automatically generates one letter flags when necessary.

`long_prefix: str` -- Default: `"--"` This sets what klarg searches for to find a flag.

`short_prefix: str` -- Default: `"-"` This sets what klarg searches for in shortened versions of a flag

`help_flag: tuple` -- Default: `("--help", "-h")` This sets what klarg looks for to display the help message.

`version_flag: tuple` -- Default: `("--version", "-v")`

Example:
```py
# docs_example.py
import klarg
settings = {
    "has_short_flags": True,
    "long_prefix": "/",
    "short_prefix": "-"
}

klarg.configure(settings)
```

#### `get_all() -> tuple`
Collects all the arguments passed and returns them all as a tuple full of strings. This is useful when a program needs to collect a list of all the arguments passed on to operate on, it passes everything single option passed to the file.

Example:
```py
# docs_example.py
import klarg

all_args = klarg.get_all()
print(f"All args {all_args}")

```

#### `get_bool(name, short) -> bool`
`name: str: NEEDED`

`short: str: optional`

`get_bool` is a function that collects `name`, a string, and `short`, also a string. `name` is the long name for the command line argument, i.e. (`--long-name`). `short` is the shorter name for the command line argument (`-s`). Normally, if `short` is not given, then it does not make one up, unless configured with `configure()`.

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

`get_num` is a function that collects a `name`, which is the multi letter flag, a `short`, which is the shortened version of the flag. There are two possible types of errors it can encounter, one being that the value it got was not a number, or that it did not get a value at all, the error names are `ERR_NUM` and `ERR_NONE` respectively. `on_error` is a dictionary, both keys, `ERR_NUM` and `ERR_NONE` are not needed. 

* num can be either an integer or a floating point

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

The `action` is run when klarg detects the help flag. What klarg looks for can be configured in the `configure()` option.

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

Klarg displays the `message` when the version flag is detected. What klarg looks for can be configured in the `configure()` option.

Example:
```py
# docs_example.py
import klarg
klarg.project_version("This project version is 1.2.3")

# python docs_example.py --version
# This project version is 1.2.3
```