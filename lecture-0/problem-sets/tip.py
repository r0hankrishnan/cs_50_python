#Main function
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#Take string and replace $ with nothing then convert to float
def dollars_to_float(d):
    cost = d.replace ("$", "")
    return float(cost)

#Take string and replace % with nothing then covert to float and divide by 100
def percent_to_float(p):
    percent = p.replace ("%", "")
    return float(percent)/100

#Call main
main()
