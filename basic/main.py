my_list = []
list_copy = None
running = True

while running:
    print("1. Add an Item")
    print("2. Remove an Item")
    print("3. Display the List")
    print("4. Undo the Previous Change")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        list_copy = my_list.copy()
        new_item = input("Enter the item to add: ")
        my_list.append(new_item)
        print(f"'{new_item}' has been added.")

    elif choice == "2":
        list_copy = my_list.copy()
        if not my_list:
            print("Your list is empty.")
        else:
            for index in range(len(my_list)):
                print(f"{index}: {my_list[index]}")
            index_to_remove = int(input("Enter the # of the item to remove: "))
            removed_item = my_list.pop(index_to_remove)
            print(f"'{removed_item}' has been removed.")

    elif choice == "3":
        print("Current List:")
        if not my_list:
            print("     ")
        for item in my_list:
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