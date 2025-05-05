# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:

  def start(self):
    print("Engine has egnited.")

class Car:  

  def __init__(self, engine): 
    self.engine = engine  


  def start_car(self):
    print("Starting the car...")
    self.engine.start()  

engine1 = Engine()

car1 = Car(engine1)

car1.start_car()