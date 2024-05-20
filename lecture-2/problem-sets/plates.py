#Prompt user for vanity plate
#Check following: start with at least two letters , no numbers in middle, first # can't be 0, no periods, spaces, or punctuation




def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() == False:
        return False
    elif len(s) <2 or len(s) >6:
        return False
    else: 
        return True


main()