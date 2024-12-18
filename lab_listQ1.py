#input 5 elements
lst = [input(f"Enter element {i+1}: ") for i in range(5)]
print("\nInitial List:", lst)

while True:
    print("\n1. Insert  2. Delete  3. Display  4. Exit")
    choice = input("Choose an operation: ")

    if choice == "1":
        elem = input("Element to insert: ")
        pos = int(input(f"Position (0-{len(lst)}): "))
        if 0 <= pos <= len(lst):
            lst.insert(pos, elem)
        else:
            print("Invalid position!")
    elif choice == "2":
        elem = input("Element to delete: ")
        if elem in lst:
            lst.remove(elem)
        else:
            print("Element not found!")
    elif choice == "3":
        print("List:", lst)
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
