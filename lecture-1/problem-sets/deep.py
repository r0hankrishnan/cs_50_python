def main():
    answer = input("What is the answer to the Great Question of Life? ")
    if great_question(answer):
        print("Yes")
    else:
        print("No")

def great_question(x):
    match x:
        case "42" | "forty-two" | "forty two":
            return True
        case _:
            return False
        
main()