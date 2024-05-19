#Prompt user for name of variable in camel case
#Iterate through str and add a _ before each uppercase then make the letter lowercase
#Print result

name = input("camelCase: ")

print("snake_case: ", end = "")
for letter in name:
    if letter.isupper():
        print("_" + letter.lower(), end = "")
    else: 
        print(letter, end = "")

print()

