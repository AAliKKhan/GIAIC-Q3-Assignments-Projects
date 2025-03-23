def add_numbers(number)-> int:
    total:int=0

    for n in number:
        total +=n

    return total

def main():
    numbers: list = list(map(int, input("Enter a list of numbers to add: ").split()))


    sum_of_numbers: int = add_numbers(numbers)
    print(sum_of_numbers)  # Print out the sum above
    

if __name__ == '__main__':
    main()