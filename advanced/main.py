my_list = []
completed_list = []
list_copy = None
running = True

while running:
    print("1. Add an Item")
    print("2. Remove an Item")
    print("3. Display the List")
    print("4. Undo the Previous Change")
    print("5. Exit")
    print("6. Replace an Item")
    print("7. Check off an Item")

    choice = input("Choose an option: ")

    if choice == "1":
        list_copy = my_list.copy()
        new_item = input("Enter the item to add: ")
        my_list.append(new_item)
        print(f"'{new_item}' has been added.")

    elif choice == "2":
        list_copy = my_list.copy()
        if not my_list:
            print("Your to-do list is empty.")
        else:
            for index, item in enumerate(my_list):
                print(f"{index}: {item}")
            try:
                index_to_remove = int(input("Enter the # of the item to remove: "))
                removed_item = my_list.pop(index_to_remove)
                print(f"'{removed_item}' has been removed.")
            except ValueError:
                print("Please enter a valid number.")
            except IndexError:
                print("That index does not exist in the list.")


    elif choice == "3":
        print("1. View To-Do List")
        print("2. View Completed List")
        view_choice = input("Which list would you like to view? ")
        if view_choice == "1":
            print("To-Do List:")
            for item in my_list:
                print(item)
        elif view_choice == "2":
            print("Completed List:")
            for item in completed_list:
                print(item)

    elif choice == "4":
        if list_copy is not None:
            my_list = list_copy.copy()
            list_copy = None
            print("Previous change undone.")
        else:
            print("There is nothing to undo.")
    elif choice == "5":
        running = False
        print("Bye bye")


    elif choice == "6":
        if not my_list:
            print("Your to-do list is empty.")
        else:
            for index, item in enumerate(my_list):
                print(f"{index}: {item}")
            try:
                index_to_replace = int(input("Enter the index of the item to replace: "))
                new_value = input("Enter the new value: ")
                my_list[index_to_replace] = new_value
                print("Item has been replaced.")
            except ValueError:
                print("Please enter a valid number.")
            except IndexError:
                print("That index does not exist in the list.")

    elif choice == "7":
        if not my_list:
            print("Your to-do list is empty.")
        else:
            for index, item in enumerate(my_list):
                print(f"{index}: {item}")
            try:
                index_to_complete = int(input("Enter the index of the item to check off: "))
                completed_item = my_list.pop(index_to_complete)
                completed_list.append(completed_item)
                print(f"'{completed_item}' has been checked off.")
            except ValueError:
                print("Please enter a valid number.")
            except IndexError:
                print("That index does not exist in the list.")