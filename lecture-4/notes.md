# Libraries

- Libraries: files of code that others (or you) have written to be reused in other projects
    - Module: library in python with 1 or more functions or features built into it
    - Main function of libraries and modules is to encourage reusability of code
    - Example of pre-installed python module: `random`

- Sometimes functions are "tucked away" into modules that you need to import before using
- Modules also have documentation that you can reference

*How to load and use a module in your own program?*
- Use `import` keyword

### Notes on generate.py
- Using `import` alone imports the entire random module
    - If you only need one function, can use syntax: `from {module} import {function}`

*When using a new module: read documentation first, then import and use*

- Command-line arguments: arguments entered in command line after file
- Can use `sys.argv` to return vector of user input in command line at time of run (see `name.py`)