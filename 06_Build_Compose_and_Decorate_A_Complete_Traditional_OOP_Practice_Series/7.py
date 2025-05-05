#  Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         # Public variable
        self._salary = salary    # Protected variable
        self.__ssn = ssn         # Private variable

    # Optional: Method to safely access the private variable
    def get_ssn(self):
        return self.__ssn


# Create an object of the Employee class
emp = Employee("Ali", 99000000, "13-45-69")

# Access public variable
print("Public - Name:", emp.name)  # ✅ Works

# Access protected variable
print("Protected - Salary:", emp._salary)  # ⚠️ Works, but not recommended outside the class

# Try to access private variable directly
try:
    print("Private - SSN:", emp.__ssn)  # ❌ Will raise AttributeError
except AttributeError as e:
    print("Error accessing private variable directly:", e)

# Access private variable using name mangling
print("Private - SSN (using name mangling):", emp._Employee__ssn)  # ✅ Works, but not recommended

# Access private variable using a getter method
print("Private - SSN (using getter method):", emp.get_ssn())  # ✅ Recommended
