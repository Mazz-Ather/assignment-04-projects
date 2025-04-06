def access_element(lst, index):
    """Returns the element at the given index or an error message if out of range."""
    if 0 <= index < len(lst):
        return f"Element at index {index}: {lst[index]}"
    return "Error: Index out of range!"

def modify_element(lst, index, new_value):
    """Modifies the element at the given index or returns an error message."""
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"Updated list: {lst}"
    return "Error: Index out of range!"

def slice_list(lst, start, end):
    """Returns a sliced portion of the list or handles out-of-range cases."""
    if 0 <= start < len(lst) and 0 < end <= len(lst):
        return f"Sliced list: {lst[start:end]}"
    return "Error: Invalid slice range!"

def main():
    # Step 1: Initialize a list with at least 5 elements
    my_list = ["Python", "JavaScript", "Java", "C++", "Swift"]

    while True:
        # Step 2: Ask the user for an operation
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            try:
                index = int(input("Enter index to access: "))
                print(access_element(my_list, index))
            except ValueError:
                print("Error: Please enter a valid number!")

        elif choice == "2":
            try:
                index = int(input("Enter index to modify: "))
                new_value = input("Enter new value: ")
                print(modify_element(my_list, index, new_value))
            except ValueError:
                print("Error: Please enter a valid number!")

        elif choice == "3":
            try:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                print(slice_list(my_list, start, end))
            except ValueError:
                print("Error: Please enter valid numbers!")

        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select a valid option.")

# Run the function
main()
    