def main():
    try:
        dividend: int = int(input("Please enter an integer to be divided: "))
        divisor: int = int(input("Please enter an integer to divide by: "))

        if divisor == 0:
            print("Error: Division by zero is not allowed.")
            return  # Exit the function safely

        quotient: int = dividend // divisor  
        remainder: int = dividend % divisor  
        
        print(f"The result of this division is {quotient} with a remainder of {remainder}")

    except ValueError:
        print("Error: Please enter valid integers.")

if __name__ == '__main__':
    main()
67