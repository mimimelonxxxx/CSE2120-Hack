"""
title: Shopping List
author: Michelle Jiang 
date-created: 2022-10-26
"""

"""
Notes: 
YOU MUST:
Use functions 
Build off of the array 
menu() with correct options 
addItems() 
for item in shoppinglist: 
    print the item on its own row 


add items to list 
1. Meat 
- Beef 
etc 
must be similar to above 
view shopping list must also allow the user to remove items 
remove index [i] when i = input 
"""

### FUNCTIONS ### 
import sys
SHOPPING_LIST = [["Meats"], ["Produce"], ["Baked Goods"], ["Dairy"]]

def checkInt(VALUE): 
    """
    checks if the value is an int
    :VALUE: str 
    :return: int 
    """
    if VALUE.isnumeric(): 
        return int(VALUE)
    else: 
        print("Please input a valid number! ")
        NEWVALUE = input("> ")
        return checkInt(NEWVALUE)

def menu(): 
    """
    prints the menu of options to choose from and prompts user to make a selection
    :return: int 
    """
    print("""
1. Add Meats 
2. Add Produce 
3. Add Baked Goods 
4. Add Dairy 
5. View Shopping List 
6. Exit
    """)
    CHOICE = input("> ")
    CHOICE = checkInt(CHOICE)
    if CHOICE > 0 and CHOICE < 7: 
        return CHOICE
    else: 
        print("Please input a valid number! ")
        return menu()

def addItem(CHOICE): 
    """
    adds item to shopping list category 
    :param CHOICE: int (user's previous selection)
    :return: str 
    """
    global SHOPPING_LIST
    # Input # 
    ITEM = input("Item: ")
    # Processing # 
    SHOPPING_LIST[CHOICE-1].append(ITEM)
    # Output # 
    print(f"{SHOPPING_LIST[CHOICE-1][-1]} added to {SHOPPING_LIST[CHOICE-1][0]} list. ")

def removeItem(): 
    """
    removes item from a category 
    :return: None
    """
    global SHOPPING_LIST
    CATEGORY = input("Category number for item to remove (leave blank to return to main menu): ")
    if CATEGORY == "": 
        return  
    else: 
        CATEGORY = checkInt(CATEGORY)
        if CATEGORY < 5: 
            for j in range(len(SHOPPING_LIST[CATEGORY-1])):
                if j == 0:
                    ITEMEDLIST = ""
                else:
                    ITEMEDLIST = f"""
{j}. {SHOPPING_LIST[CATEGORY-1][j]}
                """
                print(ITEMEDLIST)
            CHOICE = input("Item number to remove: ")
            CHOICE = checkInt(CHOICE)
            ITEM = SHOPPING_LIST[CATEGORY-1].pop(CHOICE)
            print(f"Successfully check off {ITEM}")
            return 
        else: 
            print("Please input a valid category number! ")
            return 

def viewList(): 
    """
    prints the list 
    :return: None
    """
    global SHOPPING_LIST
    for i in range(len(SHOPPING_LIST)):
        LIST = f"""
{i+1}. {SHOPPING_LIST[i][0]}
"""
        for item in SHOPPING_LIST[i]:
            if item == "Meats" or item =="Produce" or item == "Baked Goods" or item == "Dairy": 
                ITEMEDLIST = ""
            else:
                ITEMEDLIST = f"""
- {item}
            """
            LIST = LIST + ITEMEDLIST
        print(LIST)

def exitProcess():
    """
    exits the program 
    :param CHOICE: int 
    :return: None
    """
    sys.exit()

### MAIN PROGRAM CODE ### 
if __name__ == "__main__": 
    # INPUTS # 
    while True:
        CHOICE = menu()
        # PROCESSING # 
        if CHOICE < 5: 
            addItem(CHOICE)
        elif CHOICE == 5: 
            viewList()
            removeItem()
        # OUTPUTS # 
        else: 
            exitProcess()