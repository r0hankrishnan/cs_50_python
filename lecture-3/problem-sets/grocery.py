#prompt user for items, one per line, until input ctr-d
#then output grocery list in all upper, 
# sorted alphabetically by item,
# prefixing each line with the number of 
# times the user inputted that item

groceryList = {

}

def main():
    groceryList = update_groceryList()

    sortedGroceryList = sort_dict(groceryList)

    display_groceries(sortedGroceryList)


def update_groceryList():    
    while True:
        try:
            item = input("Item: ").strip().upper()
            if item in groceryList:
                groceryList[item] += 1
            else:
                groceryList[item] = 1
        except EOFError:
            print("")
            return groceryList


def sort_dict(dict):
    sortedList = sorted(dict.items())

    sortedDict = {}
    for key,value in sortedList:
        sortedDict[key] = value
    
    return sortedDict

def display_groceries(dict):
    for key,value in dict.items():
        print(f"{dict.get(key)} {key}")


main()



