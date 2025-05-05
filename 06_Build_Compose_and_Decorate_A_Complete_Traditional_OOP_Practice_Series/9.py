# '''9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().'''

# Import abc module to create abstract classes
from abc import ABC, abstractmethod

class Shape(ABC):
  
  @abstractmethod
  def area(self):
    pass  


class Rectangle(Shape):

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height  

rect = Rectangle(9, 7)  

print(f"Area of Rectangle: {rect.area()}")  