# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:

  def __init__(self, name, emp_id):
    self.name = name       
    self.emp_id = emp_id   

  def show_details(self):
    print(f"Employee Name: {self.name}, ID: {self.emp_id}")


class Department:

  def __init__(self, dept_name, employee):
    self.dept_name = dept_name    
    self.employee = employee        

  def show_department(self):
    print(f"Department: {self.dept_name}")
    self.employee.show_details()   

emp1 = Employee("Ali Khan", 307)

dept1 = Department("IT", emp1)

dept1.show_department()