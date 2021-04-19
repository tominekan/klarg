import klarg

ALL_ARGS = [
    "--some-number",
    "10",
    "--not-number",
    "1a",
    "--number-no-args"
]

assert(klarg.get_all() == ALL_ARGS)
