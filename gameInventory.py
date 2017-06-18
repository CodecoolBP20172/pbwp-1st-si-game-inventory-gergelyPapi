# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# Displays the inventory.

def display_inventory(inventory):
    print("Inventory:")
    for key, value in inventory.items():
        print("{0} {1}".format(value, key))
    total = sum(inv.values())
    print("Total number of items: {0}".format(total))


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for item in added_items:
        try:
            inv[item] = inv[item] + 1
        except KeyError:
            inv[item] = 1

display_inventory(inv)


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order


def print_table(inventory, order=None):
    first_column_width = 7
    second_column_width = get_max_width(inventory) + 4
    print("Inventory:")
    item_name = "item_name"
    count = "count"
    dash = "-"
    print (count.rjust(first_column_width, ' ') + item_name.rjust(second_column_width, ' '))
    print("-" * (first_column_width + second_column_width))
    if order == "count,desc":
        reverse = False
        print_ordered(inventory, first_column_width, second_column_width, reverse)
    elif order == "count,asc":
        reverse=True
        print_ordered(inventory, first_column_width, second_column_width, reverse)
    else:
        print_unortodox(inventory, first_column_width, second_column_width)
    print("-" * (first_column_width + second_column_width))
    total = sum(inv.values())
    print("Total number of items: {0}".format(total))

#This is the function to call if order has some input, and the ordering must be changed
def print_ordered(inventory, first_column_width, second_column_width, reverse):
    for key in sorted(inventory, key=inventory.get, reverse=reverse):
        value = inventory[key]
        print(str(value).rjust(first_column_width, ' ') + key.rjust(second_column_width, ' '))

#This is the function if the order argument left empty
def print_unortodox(inventory, first_column_width, second_column_width):
    for key,value in inventory.items():
        print(str(value).rjust(first_column_width, ' ') + key.rjust(second_column_width, ' '))

#This funciton is used to adjust the width of the columns in the table properly
def get_max_width(inventory):
    column_width = 0
    for key in inventory:
        current_length = len(key)
        if current_length > column_width:
            column_width = current_length
    return column_width

# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).

def import_inventory(inventory, filename):
    new_dragon_loot = []
    with open(filename) as inputfile:
        for line in inputfile:
            new_dragon_loot = line.strip().split(',')
    return new_dragon_loot

dragon_loot = import_inventory(inv, "test_inventory.csv")
add_to_inventory(inv, dragon_loot)

#This is just an example call

print_table(inv, "count,asc")

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).

def export_inventory(inventory, filename=None):
    export_list = []
    for key, value in inventory.items():
        export_list += ([key] * value)

    write_file = open(filename, "w")
    write_file.write(",".join(export_list))
    write_file.close()

export_inventory(inv, "test_export_inventory.csv")
