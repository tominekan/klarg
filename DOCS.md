# Klarg docs

This is where the documentation and references are.
## Overview
[Introduction](##Introduction)
[Terminology](##Terminology)
[Contributing](##Contributing)
[API Reference](##APIReference)
[Implementations](##Implementations)


## Introduction
Klarg is a small, fast (as python goes 😃) and simple command line argument parsing library built with no 3rd party dependencies.


## Terminology
There are a number of terminologies used in this documentation. A command line **switch** or **flag** is a term used to describe an option passed to the arguments of a program, examples include `-l`, or `--klarg-rocks`. These terms will be used interchangeably.


## Contributing
Check [CONTRIBUTING.md](CONTRIBUTING.md)


## API Reference
This is a list of all the methods, what they do, their arguments, and how they use them.
NOTE: anything in curly brackets "{" "}" is a variable.


#### `configure(configuration={configuration}) -> None`
Configure takes in a dictionary called `confguration`
Below is a list of values that configure takes:
`has_short_flags: bool` -- Default: `False` This controls if klarg automatically generates one letter flags when necessary.
`long_prefix: str` -- Default: `"--"` This sets what klarg searches for to find a flag.
`short_prefix: str` -- Default: `"-"` This sets what klarg searches for in shortened versions of a flag
`help_flag: tuple` -- Default: `("--help", "-h")` This sets what klarg looks for to display the help message.
`version_flag: tuple` -- Default: `("--version", "-v")`

#### `get_all() -> list`
Collects all the arguments passed and returns them all as a list full of strings. This is useful when a program needs to collect a list of all the arguments passed on to operate on, it passes everything single option passed to the file.

#### `get_bool(name={long_name}, short={short_name}) -> bool`
`get_bool` is a function that collects `name`, a string, and `short`, also a string. `name` is the long name for the command line argument, i.e. (`--long-name`). `short` is the shorter name for the command line argument (`-s`). Normally, if `short` is not given, then it does not make one up, unless configured with `configure()`.

#### `get_str(name={long_name}, short={short_name} on_error={action}) -> str`

#### `get_num(name={long_name}, short={short_name}, on_error={action}) -> int`
`get_num` is a function that collects a `name`, which is the multi letter flag, a `short`, which is the shortened version of the flag. There are two possible types of errors it can encounter, one being that the value it got was not a number, or that it did not get a value at all. on_error can have two types, a dictionary and a function. 

#### `on_help(action={action})`
The `action` is run when klarg detects the help flag. What klarg looks for can be configured in the `configure()` option.

#### `project_version(message={message})`
Klarg displays the `message` when the version flag is detected. What klarg looks for can be configured in the `configure()` option.


## Implementations
### Klarg's `short` or shortened flag generation
If a `short` variable is not given, then klarg makes one up. Klarg does this by taking the first letter of the multi letter switch, for example `--heavy` and collecting the first letter, which in this case is "-h". If it does not work due to conflictions with already set single letter flags, then it capitalizes it, if that does not work, then it appends the second letter to the first, if that does not work, it capitalizes it, if that does not work, then it deletes the second letter and appends the third letter if it is different from the second letter, else it skips it. And so on and so forth.