# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.


class Multiplier:

    def __init__(self, factor):
        self.factor = factor  


    def __call__(self, value):
        return value * self.factor  


multiply_by_5 = Multiplier(3)


print("Is object callable?", callable(multiply_by_5))  


result = multiply_by_5(110)  
print("Result of calling object:", result) 