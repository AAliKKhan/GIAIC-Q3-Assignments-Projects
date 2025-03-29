def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    return lst[start:end]  # No need for exception handling as slicing handles out-of-range cases gracefully

def index_game():
    lst = [1, 2, 3, 4, 5]  # Example list
    print("Current list:", lst)
    print("Choose an operation: access, modify, slice")
    
    operation = input("Enter operation: ").strip().lower()

    if operation == "access":
        index = int(input("Enter index to access: "))
        print("Element at index:", access_element(lst, index))
    
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        
        # Convert new_value to int if list contains numbers
        try:
            new_value = int(new_value)
        except ValueError:
            pass  # Keep it as a string if conversion fails

        print("Updated list:", modify_element(lst, index, new_value))
    
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print("Sliced list:", slice_list(lst, start, end))
    
    else:
        print("Invalid operation. Please choose access, modify, or slice.")


# Run the game
if __name__ == "__main__":
    index_game()
