# Lecture Notes -- Loops
**Lecture runs from 2:46:43 to 4:07:10**

- **Keyword**: `while`
    - Asks a question over and over until answer is `True`
    - When using a counter, make sure to add a line **inside** the while loop to update the counter
    - To get out of an infinite loop, use ctrl + C
    - **Abbr. of i = i + 1 &rarr; `i += 1`**

- **Lis**: way of containing **multiple** values within **one** variable
    - Syntax: represent lists with []
        - e.g. `range(3)` would return `[0,1,2]`
    - To index a list use square brackets next to variable name of list &rarr; **remember that python is ZERO INDEXED**
        - e.g. `x[0]` would return the first item in the list called "x"
    - Can also iterate over a list (even if it does not contain numbers)
        - e.g. `for item in x` would iterate over every item in the list called "x"
    - Common function used with lists: `len()` &rarr; returns number that is the length of list
        - e.g. `for i in range(len(list))` would iterate over the length of a list by setting i = 0, then 1, etc. 

- **Keyword**: `for`
    - Different than for loops in other languages
    - Syntax: `for i in range(#):`
    - Common function used with for loops: `range`
        - Takes one arg: the number of 'items' in range 
    - Best practice: use `_` instead of a letter when defining a variable that is **only necessary for a loop or some other function and is not being used elsewhere in your code**
    - Common practice in python when you want to get user input and have a **certain expectation**: `while True`
        - Induces an infinite loop (answer is always True), then ask question, then define if statement to filter out undesired response
    - Can nest loops

- **Dictionaries**: Variable that allows you to associate keys with values (2D object)
    - Syntax: represent dicts with {}
        - e.g. `dict = {key:value, key:value, key:value}`
        - Best practice: indent after each key:value pair to avoid text wrapping
    - To index a dict, you can use the key name in the []
        - e.g. `dict["value"]`
    - Can store dicts **inside** of list
        - e.g. `list = [{key:value, key:value},{key:value, key:value}]`
    - **Can indicate no entry in a dict by using `None`**