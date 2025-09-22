print("\n\nWelcome to my online store!")
items = []
costs = []
currentTask = 0

def printOptions():
    print("\n1: Add new item\n2: Display the contents of the shopping cart\n3: Edit an item\n4: Remove an item\n5: Compute cart total\n6: Quit")

while currentTask != 6:
    printOptions()
    currentTask = float(input("Which action would you like to do? Indicate your action with a number 1-5"))
    if currentTask == 1:
        items.append(input("What would you like to add?"))
        cost = float(input(f"And how much does {items[-1]} cost? Please put a number"))
        costs.append(round(((cost))*100)/100)
        print(f"{items[-1]} has been added to your cart for ${costs[-1]}!")
    if currentTask == 2:
        print("\nThe contents of the shopping cart are:")
        for listItemNumber in range (1, len(costs)+1):
            print(f"{listItemNumber}. {items[listItemNumber-1]} - ${costs[listItemNumber-1]}")
    if currentTask == 3:
        for listItemNumber in range (1, len(costs)+1):
            print(f"{listItemNumber}. {items[listItemNumber-1]} - ${costs[listItemNumber-1]}")
        listItemNumber = int(input(f"Which item number would you like to change? Please put a number between 1-{len(costs)}"))-1
        if listItemNumber >= len(costs) or listItemNumber <=0:
            print(f"That is not a valid number input, please try again using a number between 1-{len(costs)}")
        else:
            itemOrPrice = input(f"Are you editing the 'name' or 'price' of {items[listItemNumber]}? Answer using the options in ' '")
            if itemOrPrice == "name":
                items[listItemNumber] = input(f"What is the new name for item '{items[listItemNumber]}'?")
                print(F"This item has been changed to {items[listItemNumber]}")
            else:
                if itemOrPrice == "price":
                    costs[listItemNumber] = input(f"What is the new price for item '{items[listItemNumber]}'?")
                    print(F"This cost has been changed to {costs[listItemNumber]}")
                else:
                    print("That is an invalid input, please try again using either 'name' or 'price'")
    if currentTask == 4:
        removeItem = float(input((f"Which item would you like removed? Please put a number between 1-{len(costs)}"))) - 1
        removeItem = int(removeItem)
        print(f"length is {len(costs)} you put item {removeItem}")
        if removeItem+1 > len(costs) or removeItem < 0:
            print("That is not a valid item number, please try again")
        else:
            items.pop(removeItem)
            costs.pop(removeItem)
            print(f"item {removeItem+1} has been removed!")
    if currentTask == 5:
        haveDiscount = input("Do you have a discount? Answer with 'Y' or 'N'")
        discount=0
        if haveDiscount == "Y":
            discount = float(input("What is the discount? Please answer with integers 1-100 based on how much you get off"))
        total=0
        for listItemNumber in range (0, len(costs)):
            total += int(costs[listItemNumber])
        print(f"Your total is: ${total*(100-discount)/100}")
    if currentTask == 6:
        print("\n\nThank you for shopping with us! We wish you a swell day\n")
    if currentTask >= 7 or currentTask <= 0:
        print("This is not a valid action, please choose an action between 1-5\n")