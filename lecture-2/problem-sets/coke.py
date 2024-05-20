#Prompts user to enter a coin one at a time and inform amount due
#Only accept 25, 10, or 5 cent coins
#Once user inputs at least 50 cents, ouput how many cents in change they are owed
#Ignore any integer that isn't 25,10, or 5

def get_cents():
    while True:
        print("Please input either 5, 10, or 25 cent values")
        amt = int(input("Insert coin: "))
        if amt == 5 or amt == 10 or amt ==25:
            break
    return amt

def calc_change():
    total = 0
    while total < 50:
        amt = get_cents()
        total = total + amt
        if total < 50:
            print(f"You have", 50 - total, "cents left to pay")
        else: 
            break

    print(f"You are owed", total-50, "cents")

calc_change()