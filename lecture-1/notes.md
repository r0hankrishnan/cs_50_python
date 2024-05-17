# Lecture Notes-- Conditionals
**Lecture 1 runs from 1:50:24 to 2:46:23**

- Symbols: >, >=, <, <=, ==, !=
    -   `==` represents **equality** whereas `= `represents **assignments**
- Keyword for conditionals: **if**

- Boolean expression: "question" that has a **TRUE** or **FALSE** answer
    - Parenthesis are not necessary for if statements in python
    - Just need a colon after if statement and to indent below for conditionals

- Control flow: ability to control "flow" of code from top to bottom
- Code is read from top to bottom &rarr; each conditional is read before moving on
    - Just writing out each individual if statement is poor design
    - Introduce `elif` &rarr; builds upon answer to `if` statement (**runs only if `if` statement returns FALSE**)
    - Introduce `else` &rarr; "catch all" statement if all other conditional statements return FALSE &rarr; faster than writing out a final `if` or `elif` statement

- Parity: check if number is even or odd
    - Recall that the `%` operator returns the remained of a division
- 4th data type: **boolean** &rarr; returns only either TRUE or FALSE
- Can condense simple `if` `else` statements to one line
    - Example: `return True if n % 2 == 0 else False`
- `match` statement lets you define "cases"
    - Use `_` to create "catch-all" for all other non explicit cases
    - Use `|` symbol as "or" in match statements
    - See `house.py` for example of match statement