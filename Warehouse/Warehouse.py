"""

Program: Warehouse inventory control system
Functionality:
    - Register items to the catalog
        id (auto generate)
        title
        category
        price
        stock
    - Display Catalog
    - Display Catalog (items no of stock)
    - Update the stock of a selected item
    - Print total value of the current stock (sum (price * stock))

    - Print Differnet category 
"""


from Menu import print_menu, print_header
from Item import Item
import os
import pickle

catalog = []  # this is an empty array
id_count = 1 # this is a global variable
data_file = "catalog.data"


# method declarations

def clear():
    return os.system("cls")

def save_catalog():
    global data_file
    writer = open(data_file, "wb") # open a file to Write Binary
    pickle.dump(catalog, writer)
    writer.close() # always close the file
    print(" Data Saved!! ")

def read_catalog():
    global data_file
    global id_count

    try:
        reader = open(data_file, "rb") # open the file to Read Binary
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        last = catalog[-1] # get the last item from the array
        id_count = last.id + 1
        # OR 
        # catalog[ len(catalog) - 1 ] get the last item from the array

        how_many = len(catalog)
        print(" Loaded " + str(how_many) + " Items ")
    except:
        # when the code above crashes, we get here
        print(" *Error loading data!")

def register_item():
    global id_count # import the global variable into fn scope
    print_header(' Register new Item ')
    title = input('Please input Title: ')
    category = input('Please input Category: ')
    price = float(input('Please input Price: '))
    stock = int(input('Please input Stock: '))

    # do validations here


    # create the object
    new_item = Item() # <- how to create an object of a class
    new_item.id = id_count
    new_item.title = title
    new_item.category = category
    new_item.price = price
    new_item.stock = stock
    # print(new_item)

    id_count += 1
    catalog.append(new_item)
    print(" Item created! ")

def display_catalog():
    num_items = len(catalog) # <- get the length of array or string
    print_header(' Your catalogue contains ' + str(num_items) + ' Items')
    
    print('|ID  |   Title              | Category        |     Price | Stock ')
    print('-' * 80)


    for item in catalog:        
        print("|" + str(item.id).ljust(3) +
            " | " + item.title.ljust(20) 
            + " | " + item.category.ljust(15) 
            + " | " + str(item.price).rjust(9) 
            + " | " + str(item.stock).rjust(5) )

    print('-' * 80)

def display_no_stock():
    print_header(' This is your Catalog ')    
    print('  Title              | Category        |     Price | Stock ')
    print('-' * 80)


    for item in catalog:
        if(item.stock == 0):
            print(item.title.ljust(20) 
                + " | " + item.category.ljust(15) 
                + " | " + str(item.price).rjust(9) 
                + " | " + str(item.stock).rjust(5))
    print('-' * 80)

def update_stock():
    # show all the items
    # ask the user to choose an id
    # validate the selected id
    # ask for the new stock value
    # update the stock value of the selected item

    display_catalog() # show all the items
    selected = int(input(' Please select the ID to update: '))

    found = False
    for item in catalog:
        if (item.id == selected):
            new_stock = input(' Please input new stock value: ')
            item.stock = int(new_stock)
            found = True
            print(' Stock updated!! ')

    if(found == False):
        print(' ** Error: Selected ID does not exist, try again')

def print_stock_value():
    print_header(" Current Stock Value")


    total = 0.0
    for item in catalog:
        total += (item.price * item.stock)
    print(" Total value: " + str(total))    

def remove_item():
    # show the list of items
    #ask the user to choose an id to remove
    # validate the id 
    # remove that item

# show the list of items
	display_catalog()
	#ask the user to choose an id to remove
	remove_id = int(input("Please select the ID to remove: "))
	# validate the id
	found = False
	for item in catalog:
		if(item.id == remove_id):
			# remove that item
			found = True
			catalog.remove(item)
	if(not found):
		print(' ** Error: Selected ID does not exist, try again')



# my solution 
# def remove_item():   
#    display_catalog()
#     selected = int(input(' Please select the ID to remove: '))

#     takeaway = False
#     for item in catalog:
#         if (item.id == selected):            
#             takeaway = True
#             catalog.remove(item)
        
    
#     if(takeaway == False):
#         print(' ** Error: Selected ID does not exist, try again')       
   

def list_categories():
    print_header(" List of categories used on the system")
    already_printed = []
    for item in catalog:
        if not item.category.lower() in already_printed:
            print(item.category)
            already_printed.append(item.category.lower())

# load data
read_catalog()

#loop to display menu

opc = ''
while(opc != 'x'):
    clear()
    print_menu()
    opc = input('Select an option: ')

    if(opc == '1'):
        register_item()
        save_catalog()
    elif(opc == '2'):
        display_catalog()
    elif(opc == '3'):
        display_no_stock()
    elif(opc == '4'):
        update_stock()
        save_catalog()
    elif(opc == '5'):
        print_stock_value()
    elif(opc == '6'):
        remove_item()
        save_catalog()
    elif(opc == '7'):
        list_categories()

    input('Press Enter to continue...')