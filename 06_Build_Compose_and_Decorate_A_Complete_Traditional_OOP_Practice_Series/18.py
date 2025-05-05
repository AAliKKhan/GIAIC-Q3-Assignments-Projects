# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):

        self._price = price

    @property
    def price(self):
        print("Getting the price...")
        return self._price


    @price.setter
    def price(self, new_price):
        print("Setting the price...")
        if new_price >= 0:
            self._price = new_price
        else:
            print("Price cannot be negative!")


    @price.deleter
    def price(self):
        print("Deleting the price...")
        del self._price

p = Product(10)


print("Price:", p.price)


p.price = 15
print("Updated Price:", p.price)


p.price = -50  

del p.price