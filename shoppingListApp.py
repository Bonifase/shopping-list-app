shoppingList = []
        
def help_instruc():
    print("-------------------------------------------------------")
    print("type Complete to complete the list                           |")
    print("type Show to show the list                             |")
    print("type Help for a help about these commands      |")
    print("-------------------------------------------------------")

    
def print_shopping_list():
    print("---------------")
    print("Shopping List:")
    print("---------------")
    for item in shoppingList:
        print("> " + item)