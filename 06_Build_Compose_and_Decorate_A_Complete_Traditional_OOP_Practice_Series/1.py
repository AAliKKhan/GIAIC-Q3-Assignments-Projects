class Student:
    def __init__ (self,name,marks):
        self.name= name
        self.mark= marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

student1= Student("Ali",100)
student1.display