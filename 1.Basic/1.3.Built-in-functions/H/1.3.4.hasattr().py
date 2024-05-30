'''
The hasattr() function in Python is used to determine if an object has a particular attribute. 
It returns True if the attribute exists, and False otherwise. 
This function is useful for checking the presence of attributes before attempting to access them, 
which can help prevent AttributeError exceptions.
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of Person
person = Person("Alice", 30)

# Check if the 'name' attribute exists
print(hasattr(person, 'name'))  # Output: True

# Check if the 'address' attribute exists
print(hasattr(person, 'address'))  # Output: False
