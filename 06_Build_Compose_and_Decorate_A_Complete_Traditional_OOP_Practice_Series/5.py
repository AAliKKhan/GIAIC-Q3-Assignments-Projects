# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    
    @staticmethod
    def add(a, b):
     return a + b 
    
result = MathUtils.add(56, 44)

print(f"The sum is:", result)