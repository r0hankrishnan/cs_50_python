def main():
    x= int(input("x: "))
    if is_even(x):
        print("even")
    else:
        print("odd")


#Determine if x is even or odd
def is_even(n):
    return n % 2 == 0
    
main()
