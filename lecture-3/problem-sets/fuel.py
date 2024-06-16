#Prompt user for a fraction, formatted as X/Y
#X and Y must each be integer
#Output X/Y as a % rounded to 2
#If 1% or less remains, output "E"
#If 99% or more remains, output "F"
#If X or Y is not an integer, X>Y, or Y = 0, prompt again

def main():
    x = get_frac("Fraction: ")
    print(x)

def get_frac(prompt):
    while True:
        try:
            x,y = input(prompt).split("/")
            if int(x) > int(y):
                pass
            elif 0 <= int(x)/int(y) <= 0.1:
                return("E")
            elif int(x)/int(y) >= 0.99:
                return("F")
            else:
                return(str(round(int(x)/int(y),2) * 100) + "%")
        except (ValueError, ZeroDivisionError):
            pass

main()