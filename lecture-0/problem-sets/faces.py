#Define main
def main():
    x = input(": ")
    x = x.split()
    convert(x)
    print(" ".join(x))


#Define convert 
def convert(arg):
    for word in range(0,len(arg),1):
        if arg[word] == ":)":
            arg[word] = "🙂"
        elif arg[word] == ":(":
            arg[word] = "🙁"

#Call main
main()
