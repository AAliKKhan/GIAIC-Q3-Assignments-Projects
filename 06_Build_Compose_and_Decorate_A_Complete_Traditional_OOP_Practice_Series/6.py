# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:

  def __init__(self):
    print("Logger object has been created.") 


  def __del__(self):
    print("Logger object is being destroyed.")  


log: Logger = Logger()  


del log  