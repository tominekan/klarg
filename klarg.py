import sys

# All the command line arguments
ALL_ARGS = sys.argv[1: len(sys.argv)]

# The configuration settings, this can be changed with the config function
CONFIG = {
    "has_short_flags": False,
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
