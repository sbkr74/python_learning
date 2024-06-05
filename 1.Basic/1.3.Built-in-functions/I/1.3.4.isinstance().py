# The isinstance() function in Python 3 is used to check if an object is an instance of a specified class or of a subclass.
x = 5
print(isinstance(x, int))  # Output: True
y = 'Hello'
print(isinstance(y, (float, int, str, list, dict, tuple)))  # Output: True

class MyObject:
    name = "John"

z = MyObject()
print(isinstance(z, MyObject))  # Output: True

# Here’s an example demonstrating isinstance() with inheritance:
# Define a parent class
class Animal:
    pass

# Define a subclass that inherits from Animal
class Dog(Animal):
    pass

# Create an instance of Dog
my_dog = Dog()

# Check if my_dog is an instance of Dog (True)
print(isinstance(my_dog, Dog))  # Output: True

# Check if my_dog is an instance of Animal (True)
print(isinstance(my_dog, Animal))  # Output: True

# Check if my_dog is an instance of a parent class (object) (True)
print(isinstance(my_dog, object))  # Output: True
