#Create function to take in a name and print "hello, name"
def hello(to):
    print("hello,", to)

#Define name variable
name = input("What's your name? ")

#Pass name to "to" argument in created function hello()
hello(name)

#Create a function that says bye to a name or to world if no input arg
def bye(to = "world"):
    print("bye", to)

bye()
