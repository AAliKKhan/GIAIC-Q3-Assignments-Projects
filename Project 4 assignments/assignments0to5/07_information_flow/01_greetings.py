def main():
    name : str = input("What's your name? ")
    print(greet(name))

def greet(name):
    return "Good Morning " + name + "!"
	
if __name__ == '__main__':
    main()
