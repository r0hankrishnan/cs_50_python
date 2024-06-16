#Prmpt for item, one per line, until user inputs ctr-d
#After each inputted item, display the total cost 
# of all items inputted thus far, prefixed with $ and to 2 dec
#Treat input case-sensitively
#Ignore any non-item input
#Assume every item is title cased

menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

total = 0


def get_running_total(prompt):
    while True:
        try:
            item = input(prompt).title().strip()
            sum = total + menu[item]
            print("Total: $", str(sum))

        except KeyError:
            pass

        except EOFError:
            print()
            break

get_running_total("Item: ")