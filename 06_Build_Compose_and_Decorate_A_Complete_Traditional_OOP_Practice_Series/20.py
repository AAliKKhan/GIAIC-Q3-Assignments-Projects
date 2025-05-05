# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.


class InvalidAgeError(Exception):

    def __init__(self, message="Age must be 18 or older to apply for driving lisence."):
        super().__init__(message)  


def check_age(age):
    if age < 18:
      
        raise InvalidAgeError(f"Invalid age: {age}. You must be at least 18.")
    else:
        print("Age is valid. You are eligible for lisence.") 


try:
    user_age = int(input("Enter your age: ")) 
    check_age(user_age)                      
except InvalidAgeError as e:
    print("Custom Exception Caught:", e)     
except ValueError:
    print("Please enter a valid number.")   