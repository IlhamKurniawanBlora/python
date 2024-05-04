def search_update_delete(my_dict):
    print("Options:")
    print("1. Search")
    print("2. Update")
    print("3. Delete")
    choice = int(input("Enter your choice (1/2/3): "))
    if choice == 1:
        key = input("Enter the key to search: ")
        if key in my_dict:
            print(f"Value: {my_dict[key]}")
        else:
            print("Key not found")
    elif choice == 2:
        key = input("Enter the key to update: ")
        if key in my_dict:
            new_value = input("Enter the new value: ")
            my_dict[key] = new_value
            print("Value updated")
        else:
            print("Key not found")
    elif choice == 3:
        key = input("Enter the key to delete: ")
        if key in my_dict:
            del my_dict[key]
            print("Key deleted")
        else:
            print("Key not found")
    else:
        print("Invalid choice")

my_dict = {
    "Name": "Ashutosh Krishna",
    "Roll": 23,
    "Subjects": ["OS", "CN", "DBMS"]
}

search_update_delete(my_dict)