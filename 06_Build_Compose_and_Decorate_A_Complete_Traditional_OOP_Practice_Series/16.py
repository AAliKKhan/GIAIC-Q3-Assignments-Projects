# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello()
def log_function_call(func):

    def wrapper():
        print("Function is called")  
        func() 
    return wrapper  

# Define a function and apply the decorator using @ syntax
@log_function_call
def say_hello():
    print("Hello, Fellas!")

say_hello()