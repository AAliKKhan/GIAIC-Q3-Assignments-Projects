def print_number_info(num):
    ones_digit = num % 10 
    num_digits = len(str(abs(num)))  
    print(f"The number has {num_digits} digit(s)")
    print(f"The ones digit is {ones_digit}")

def main():
    num = int(input("Enter a number: "))  
    print_number_info(num)  


if __name__ == "__main__":
    main()
