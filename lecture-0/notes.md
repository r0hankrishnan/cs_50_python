# Lecture Notes -- Functions & Variables
 **Lecture 0 runs from 0:4:48 to 1:50:24**

## Table of Contents
1. [The Basics](#basics-)
2. [Strings](#strings-)
3. [Variables](#variables-)
4. [Comments](#comments-)
5. [Functions & Parameters](#functions-)
6. [Methods](#methods-)
7. [Integers](#integers-)
8. [Float](#float-)
9. [Creating Custom Functions](#customize-)


 ## The Basics <a name="basics"></a>
- Python is a general purpose programming language
- It is very popular and has "high-level" syntax
    - High-level = closer to human language
- Python code is frequently written in a text editor
    - Using VS Code but can be anything (even MS Word if saved in the right format)
- Computers can only read and execute *binary*, meaning that we need to install a program (called the **python interpreter**) to take our python code and convert it into binary

## Strings <a name="strings"></a>
- Strings are a basic data type in python --> denoted by being surrounded by " "
    - Strings can be anything as long as it is inside of the double (or single, just be consistent) quotes

## Variables <a name="variables"></a>
- Container for *some* value inside of your computer's memory
- In python `=` is used to **assign** a value to a variable
    - `name = input("what's your name?")` stores the answer to the question "what's your name?" into the variable `name`
- You can update values of variables by writing a subsequent line of code with the `=` operator

## Comments <a name="comments"></a>
- It is important to **comment** your code so you and others can tell what you're trying to do
    - Comment using `#` symbol on each line you want to write a comment 
    - Try to comment every 2-3 lines of code to keep clean, readable code
- **Psuedocode**: "Directions" written in common english as comments to map out what you want to do with your code

## Functions & Parameters <a name="functions"></a>
- Functions in python all have documentation
    - Take the print() function for example:
    `print(*objects, sep = ' ', end = '\n', file = sys.stdout, flush = False)`
        - The * means that print() can take as many objects as you want
        - `sep = ' '` specifies the separator between each object in print()
        - `end = \n'` specifies what the computer should do at the end of the printed statements
        - `sep`, `end` are examples of the **parameters** of a function -- values you can override/change to adjust the output of a function

## Methods 
- **Methods** are functions that are specific to data types
    - They are designed to be able to manipulate or perform actions on its data type
    - Syntax: `variable.method()`
        - Example: `name = input("Name?")`
        `name = name.strip()` assigns a `str` to `name` and then uses a method `strip()` to remove whitespace from the left and right of `name`
- You can chain methods together-- be careful that your code remains balanced between concisesness and clarity
    -Example: `name = name.strip().title()`

## Integers<a name="integers"></a>
- Another basic and very common data type in python
- Any whole number from positive to negative infinity
- Python supports several `int` operators:
    - +, -, *, /, %
        - % returns the remainder when dividing two `int` values

## Float <a name="float"></a>
- Number with a decimal point-- any real number

## Creating Custom Functions <a name="customize"></a>
- Use the keyword `def` to **create** your own function
    - Syntax: `def functionName():` and then define function by writing out process **indented** below
- You can also pre-set a value for an `arg` in a function: `def: functionName(arg = "value")`
    - Can still be overwritten if new value is specified when function is called
- *Note the python interpreter reads from **top to bottom** so you must **define** functions before actually calling them*
- Scope: A variable stored within a function will only exist **within** that function
- Another important keyword is `return` which can be used in functions to tell python that you want an action/value to be displayed or returned to the screen
