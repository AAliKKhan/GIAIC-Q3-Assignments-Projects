MAX_LENGTH: int = 3  

def shorten(lst: list) -> None:

    while len(lst) > MAX_LENGTH:
        print(lst.pop()) 

def get_lst() -> list:
    lst = []
    while True:
        elem = input("Enter an element (press Enter to stop): ").strip()
        if elem == "":
            break 
        lst.append(elem)
    return lst

def main() -> None:

    lst = get_lst()
    print("\nOriginal List:", lst)
    shorten(lst)
    print("Final List:", lst)  

if __name__ == "__main__":
    main()
