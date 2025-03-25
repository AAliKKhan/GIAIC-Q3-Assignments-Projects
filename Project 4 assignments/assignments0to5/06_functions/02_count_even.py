def count_even():
    lst = []
    
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        if user_input.isdigit() or (user_input[0] == '-' and user_input[1:].isdigit()):
            lst.append(int(user_input))

    even_count = sum(1 for num in lst if num % 2 == 0)
    
    print("Number of even numbers:", even_count)


if __name__ == "__main__":
    count_even()
