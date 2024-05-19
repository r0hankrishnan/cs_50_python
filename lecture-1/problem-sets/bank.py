#If greeting contains hello, return 0
#If greeting starts with h, return $20
#Else return $100
def main():
    greeting = input("Greeting: ")
    check_greeting(greeting)

def check_greeting(x):
    if x.find("hello") == 0:
        print("$0")
    elif x.find("h") == 0: 
        print("$20")
    else:
        print("$100")

main()