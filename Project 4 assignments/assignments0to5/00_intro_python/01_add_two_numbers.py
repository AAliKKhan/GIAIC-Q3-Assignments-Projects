def add():
    print("Enter Numbers to add")
    num1 = int(input("Input 1st Number: ")) 
    num2 = int(input("Input 2nd Number: "))  
    addition = num1 + num2
    print("The total is " + str(addition) + ".")

if __name__ == "__main__":  
    add()
