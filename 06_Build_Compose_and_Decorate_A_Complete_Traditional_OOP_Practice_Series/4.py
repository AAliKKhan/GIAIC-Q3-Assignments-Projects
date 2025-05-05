# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.  

class Bank:

  bank_name = "Askari Bank"

  @classmethod
  def change_bank_name(cls, name):
    cls.bank_name = name 


  def display_bank_name(self):
    print(f"Bank Name: {Bank.bank_name}")  


customer1 = Bank()
customer1.display_bank_name()  

Bank.change_bank_name("Swiss Bank")


customer1.display_bank_name() 
