#Prompt user for x, y, z where x and z are numbers and y is operator
#Separate x, y, and z
#Convert x and z to int
#Display x y z as float
expression = input("Expression: ")
x = float(expression.split()[0])
y = expression.split()[1]
z = float(expression.split()[2])

if y == "+":
    print(x + z)
elif y == "-": 
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)
else:
    print("Math expression not recognized")
