def list_operations():
    my_list = []
    print("\n--- List Operations ---")
    print("1. Insert")
    print("2. Update")
    print("3. Delete")
    print("4. Display")
    print("5. Sort")
    print("6. Search")
    print("7. Exit")

    while True:
        choice = input("Enter choice: ")

        if choice == '1':
            value = input("Enter value to insert: ")
            my_list.append(value)
        elif choice == '2':
            old = input("Enter value to update: ")
            if old in my_list:
                new = input("Enter new value: ")
                my_list[my_list.index(old)] = new
            else:
                print("Value not found.")
        elif choice == '3':
            value = input("Enter value to delete: ")
            if value in my_list:
                my_list.remove(value)
            else:
                print("Value not found.")
        elif choice == '4':
            print("List contents:", my_list)
        elif choice == '5':
            my_list.sort()
            print("Sorted List:", my_list)
        elif choice == '6':
            search = input("Enter value to search: ")
            print("Found!" if search in my_list else "Not found.")
        elif choice == '7':
            break
        else:
            print("Invalid choice.")

def tuple_operations():
    my_tuple = ("apple", "banana", "cherry")
    print("\n--- Tuple Operations (Immutable) ---")
    print("Original Tuple:", my_tuple)
    print("1. Display")
    print("2. Search")
    print("3. Convert to List and Add Item")
    choice = input("Enter choice: ")

    if choice == '1':
        print("Tuple Contents:", my_tuple)
    elif choice == '2':
        item = input("Enter item to search: ")
        print("Found!" if item in my_tuple else "Not found.")
    elif choice == '3':
        item = input("Enter item to add: ")
        temp = list(my_tuple)
        temp.append(item)
        my_tuple = tuple(temp)
        print("Updated Tuple:", my_tuple)
    else:
        print("Invalid choice.")

def set_operations():
    my_set = set()
    print("\n--- Set Operations ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Search")
    print("5. Exit")
    while True:
        choice = input("Enter choice: ")

        if choice == '1':
            value = input("Enter value to insert: ")
            my_set.add(value)
        elif choice == '2':
            value = input("Enter value to delete: ")
            my_set.discard(value)
        elif choice == '3':
            print("Set contents:", my_set)
        elif choice == '4':
            value = input("Enter value to search: ")
            print("Found!" if value in my_set else "Not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

def dict_operations():
    my_dict = {}
    print("\n--- Dictionary Operations ---")
    print("1. Insert")
    print("2. Update")
    print("3. Delete")
    print("4. Display")
    print("5. Search")
    print("6. Exit")
    while True:
        choice = input("Enter choice: ")

        if choice == '1':
            key = input("Enter key: ")
            value = input("Enter value: ")
            my_dict[key] = value
        elif choice == '2':
            key = input("Enter key to update: ")
            if key in my_dict:
                value = input("Enter new value: ")
                my_dict[key] = value
            else:
                print("Key not found.")
        elif choice == '3':
            key = input("Enter key to delete: ")
            if key in my_dict:
                del my_dict[key]
            else:
                print("Key not found.")
        elif choice == '4':
            print("Dictionary contents:", my_dict)
        elif choice == '5':
            key = input("Enter key to search: ")
            print("Found!" if key in my_dict else "Not found.")
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

# Main Program Loop
print("\n===== Main Menu =====")
print("1. List")
print("2. Tuple")
print("3. Set")
print("4. Dictionary")
print("5. Exit")

while True:    
    main_choice = input("Enter Choice: ")

    if main_choice == '1':
        list_operations()
    elif main_choice == '2':
        tuple_operations()
    elif main_choice == '3':
        set_operations()
    elif main_choice == '4':
        dict_operations()
    elif main_choice == '5':
        print("Exiting Program.")
        break
    else:
        print("Invalid choice. Try again.")
