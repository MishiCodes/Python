print ("Welcome to the Shopping List application")

"""Dictionary to get individual item details"""
current_item = {}

"""List to keep track of items"""
grocery_history = []
stop = False

"""iterates to get items details until user press 'n'"""
while not stop:
    name = input("Enter item name: ")
    quantity = int(input("Enter item quantity: "))
    cost = float(input("Enter item cost: "))

    """Populating dictionary with item details"""
    current_item = {
        'item_name': name,
        'item_quantity': quantity,
        'item_cost': cost
    }

    """Populating list with items"""
    grocery_history.append(current_item)
    """Getting user response whether they need to continue adding items or quit"""
    response = input(("Would you like to enter another item?\n Enter 'y' to continue and 'n' to exit: "))
    if response == 'n':
        stop = True

grand_total = 0
"""Iterating over grocery list to calculate each item total and total bill"""
for item in grocery_history:
    item_total = item['item_quantity'] * item['item_cost']
    grand_total += item_total
    """Printing item name with cost of each item and total for each item"""
    print("%d %s for  %.2f each  %.2f" % (item['item_quantity'], item['item_name'], item['item_cost'], item_total)) 
    print()
    item_total = 0
print ('-' * 35)
"""Printing total bill"""
print("Total                      %.2f sek" % grand_total)
