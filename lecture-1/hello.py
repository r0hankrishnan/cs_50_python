#Working with inputs, strings, and methods

#Ask for name and store in a variable
name = input("what is your name? ")

#Remove white space from start and end and capitalize
name = name.strip().title()

#Split into first and last name
first,last = name.split(" ")

#Output a message that says "hello, " and the input name
print("hello,", name) 

#Output a message that tells you your first and last name
print("Your first name is", first, "and your last name is", last)
