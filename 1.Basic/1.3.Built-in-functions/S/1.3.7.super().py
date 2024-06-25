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