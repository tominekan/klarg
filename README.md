# Klarg

A Kommand Line ARGument parsing library.

# Features
Klarg is a small, fast (as python goes 😃) and simple command line argument parsing library built with no 3rd party dependencies.

# How to use
```py
# example.py
import klarg
klarg_is_cool = klargs.get_bool(long="klarg-cool", short="k")
klargs.on_help(do_something)

if (klarg_is_coool):
    print("Oh, my, klarg is cool.")

# python example.py --klarg-cool
# Oh, my, klarg is cool.

# python example.py -k
# Oh, my, klarg is cool.
```

Check out the [Documentation](DOCS.md)