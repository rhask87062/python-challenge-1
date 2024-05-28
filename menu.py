# Create a tuple containing the names of menu sections:
# snacks, meals, drinks, and dessert.
menu_categories= ("snacks", "meals", "drinks", "dessert")

# Print the tuple.
print(menu_categories)

# Create a list of items for one of the menu sections.
desserts = [
    ["Black Forest Cake", 4.99],
    ["Pavlova", 6.99],
    ["Lemon Meringue Pie", 4.25],
    ["Cherry Tart", 3.55]
]

# Create a list of prices for each of the menu items in the previous list.

# Ask a user to input a new item.
new_dessert_name = input("What's the name of the new dessert? ")

# Ask a user to input the price of the new item.
new_dessert_price = float(input("What's the price of the new dessert? "))

# Append the list with the new item and price entered by the user.
desserts.append([new_dessert_name, new_dessert_price])

# Print out confirmation of added dessert, and prints out the menu.
print(f"The new dessert '{new_dessert_name}' has been added to the menu.")
print(f"Here is the updated desserts menu:\n {desserts}")

# Ask the user which item to remove from the menu.
remove_item = input("Which item do you want to remove? ")

# Iterate through the list of lists
for i, dessert in enumerate(desserts):
    if dessert[0] == remove_item:  # Check if the first element (dessert name) matches
        del desserts[i]           # Delete the entire sublist at that index
        print(f"{remove_item} has been removed from the menu.")
        break                      # Stop the loop after removing the item
else:                             # This block executes if the item is not found
    print(f"Error: '{remove_item}' is not in the menu.")

# Print the menu and prices again to confirm removal.
print(desserts)

# Find the most expensive price on the menu.
print(f"Most expensive: {max(desserts)}")

# Find the cheapest price on the menu.
print(f"Cheapest: {min(dessert_prices)}")

# Find the cost if someone bought every item on the menu.
print(f"Total cost: {sum(dessert_prices)}")

# Confirm that the menu and prices lists are the same length.
print(f"The menu length is {len(desserts)}, and the prices length is {len(desserts)}")

#Create an empty list. This will later store a customer's order in dictionary format.
order = []

# Get user's order choice
print("Menu:\n")
for i, item in enumerate(desserts, start=1):
    name, price = item
    print(f"{i}. {name} - ${price:.2f}")
menu_selection = int(input("Enter the number of the item you want to order: "))
 order.append(desserts[int(menu_selection) - 1])


while True:
    order = []

    print("Menu:\n")
    if item_number, item_info in desserts.items():
        print(f"{item_number}. {item_info['name']} - ${item_info['price']:.2f}")
            
#If the user input is not in the menu_items keys, print an error. Otherwise, perform the following actions:
    #-Get the item name from the menu_items dictionary and store it as a variable.
    #-Ask the customer for the quantity of the menu item, using the item name variable in the question, and let them know that the quantity will default to 1 if their input is invalid. Save their answer as a variable called quantity.
    #-Check that the customer input is a number. If it isn't, set the quantity to the value 1. If it is a number, convert the variable to an integer.
    #-Append the customer's order to the order list in dictionary format with the following keys: "Item name", "Price", and "Quantity. You will need this information to print the receipt at the end of the order. The price should be found in the menu_items dictionary.
if 7

#Inside the continuous while loop that prompts the customer if they would like to keep ordering, write a match:case statement that checks for y or n (upper or lowercase), and includes a default option if neither letter is entered by the customer. The following actions should be performed for each case:
    #-y: Set the place_order variable to True and break from the continuous while loop.
    #-n: Set the place_order variable to False, print "Thank you for your order", and break from the continuous while loop.
    #-Default: Tell the customer to try again because they didn't type a valid input.


#Create a for loop to loop through the order list.


#Inside the loop, save the value of each key as their own variable: item_name, price, and quantity.


#Calculate the number of empty spaces that should be added to the display so that the receipt uses the following format:
#Item Name          | Price | Quantity
#--------------------------------------
#Apple              | $0.49 | 1
#Tea - Thai iced    | $3.99 | 2
#Fried banana       | $4.49 | 3


#Create the spaces as their own variables using string multiplication.


#Print the line for the receipt using the format in step 8.


#Upon exiting the for loop, use list comprehension and sum() to calculate the total price of the order and display it to the customer. Make sure you multiply the price  by the quantity of your list comprehension.


######~~~Hints and COnsiderations~~######
#-Consider what you've learned so far. You've learned how to store content3 in variables, lists, and dictionaries. You've learned how to iterate through data structures, and you've learned how to debug along the way. Using all that you've learned, try to break down your tasks into discrete mini-objectives
#-If you're struggling with how to start, consider writing out the steps of the process using pseudocode
#-Always commit your work and back it up with pushes to GitHub or GitLab. You don't want to lose hours of your hard work! Also make sure that your repo has a detaild readme.md file.77