MINIMUM_HEIGHT : float = 50 

def main():
    height:float=float(input("Enter your height in inches : "))
    if height  >= MINIMUM_HEIGHT:
        print("You are eligible for ride")
    else:
        print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()