#  The function deletes the named attribute, provided the object allows it. 
# For example, delattr(x, 'foobar') is equivalent to del x.foobar. 

'''
delattr() is a built-in Python function used to delete attributes from objects. 
It takes two arguments: the object from which to delete the attribute and the name of the attribute to delete. 
'''
class MyClass:
    def __init__(self):
        self.x = 10
        self.y = 20

obj = MyClass()
print("Before deletion:", obj.__dict__)  # Output: {'x': 10, 'y': 20}

delattr(obj, 'x')

print("After deletion:", obj.__dict__)  # Output: {'y': 20}

# Example 1:

'''
Removing Unnecessary Attributes: Sometimes, during the lifecycle of an object, 
certain attributes become irrelevant or need to be removed. 
delattr() provides a convenient way to remove such attributes.
'''
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.temp_data = None  # Temporary data not needed after initialization

user = User("john_doe", "john@example.com")
# ... do something with user.temp_data ...
delattr(user, 'temp_data')  # Remove temp_data after it's no longer needed


# Example 2:
'''
Dynamic Attribute Handling: Sometimes, attributes need to be dynamically added or removed based on runtime conditions or user input.
'''

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

car = Car("Toyota", "Corolla")
user_decision = input("Enter the choice: ")
# User decides to remove 'model' attribute
if user_decision == 'remove_model':
    delattr(car, 'model')
