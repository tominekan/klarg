import sys

# All the command line arguments
ALL_ARGS = sys.argv[1: len(sys.argv)]

# The configuration settings, this can be changed with the config function
CONFIG = {
    "needs_short_flags": False,
    "long_prefix": "--",
    "short_prefix": "-",
    "help_flag": ("--help", "-h"),
    "version_flag": ("--version", "-v")
}


def get_all() -> list:
    """
    Collects all the arguments passed and returns them all as a tuple
    full of strings. This is useful when a program needs to collect
    a list of all the arguments passed on to operate on,
    it passes everything single option passed to the file

    Example:
`   ```py
    # docs_example.py
    import klarg

    all_args = klarg.get_all()
    print(f"All args {all_args}")

    # python docs_example.py -a -b "c" -d --efgh --ijklmn 0
    # All args ("-a", "-b", "c", "-d", "--efgh", "--ijklmn", "0")
    ```

    """

    return ALL_ARGS


def get_bool(name: str, short: str = "default") -> bool:
    """
    `name: str: NEEDED`

    `short: str: optional`

    `get_bool` is a function that collects `name`, a string, and `short`,
    also a string. `name` is the long name for the command line argument,
    i.e. (`--long-name`). `short` is the shorter name for the command
    line argument (`-s`). Normally, if `short` is not given,
    then it will not raise an error, unless `"needs_short_flags"`
    is set to `True` in `CONFIG`.

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

    """

    if short == "default":
        if (CONFIG["needs_short_flags"]):
            raise Exception(
                "No short flag for get_bool()"
            )

    if (name in ALL_ARGS) or (short in ALL_ARGS):
        return True
    else:
        return False
