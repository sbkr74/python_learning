class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name) 
        self.age = age

    def greet(self):
        super().greet()  
        print(f"And I'm {self.age} years old")

# Create an instance of Child
child = Child("Shubham Biruly", 25)
child.greet()

######################################################
''' Using super() for method overriding'''
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print(f"{self.__class__.__name__} Bark")

dog = Dog()
dog.sound()

#################################################################
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def work(self):
        print(f"{self.name} is working with a salary of {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        # Call the parent class's constructor using super()
        super().__init__(name, salary)
        self.department = department
    
    def work(self):
        # Call the parent class's work method using super()
        super().work()
        print(f"{self.name} is managing the {self.department} department")

# Create an instance of Employee
emp = Employee("Shubham", 50000)
emp.work()
# Output: Shubham is working with a salary of 50000

# Create an instance of Manager
mgr = Manager("Biruly", 70000, "IT")
mgr.work()
# Output:
# Biruly is working with a salary of 70000
# Biruly is managing the IT department
