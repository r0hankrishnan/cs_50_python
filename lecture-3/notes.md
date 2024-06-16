# Exceptions
- Refers to problems in your code
    - When something is an exception, it means it is not working or is a problem
    - Example: `print("hello, world)` returns SyntaxError: unterminated string literal because we didn't close the quotes

- Can error-proof code using `try` and `except` (see number.py)
    - Syntax is try: (indent) code \n except Name of error: code
    - Also supports `else`
        - Can use this to define case if try succeeds for clearer code

- If you want to handle/catch an exception without actually building an alternative scenario, can use `pass` in `except:` statement (see number.py)

- Can feed parameters into user-defined function to allow for more specificity and customizability