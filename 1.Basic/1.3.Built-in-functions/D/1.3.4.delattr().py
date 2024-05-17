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

class MyClass:
    def __init__(self, x):
        self.x = x

obj = MyClass(5)

# Dynamically delete an attribute based on user input
attribute_name = input("Enter the attribute name to delete: ")
if hasattr(obj, attribute_name):
    delattr(obj, attribute_name)

print(obj.__dict__)


class Config:
    def __init__(self):
        self.host = "localhost"
        self.port = 8080

config = Config()

# Dynamically change configuration
config.host = "example.com"
config.port = 9090

# Remove outdated configuration
delattr(config, 'port')


# Example 3:
'''
Cleaning Up Resources: In some cases, attributes may represent resources that need to be cleaned up when no longer needed, 
such as file handles or network connections.
'''
class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename, 'r')

    def close_file(self):
        self.file.close()

file_handler = FileHandler("example.txt")
# ... do something with file_handler.file ...
delattr(file_handler, 'file')  # Close file handle when no longer needed

# Example 4: Deleting a method from a class:
'''

'''
class MyClass:
    def method(self):
        print("This is a method")

delattr(MyClass, 'method')
obj = MyClass()
# Raises AttributeError: 'MyClass' object has no attribute 'method'
obj.method()

# Example 5: Deleting a property from a class:
'''
'''
class MyClass:
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

delattr(MyClass, 'value')
obj = MyClass()
# Raises AttributeError: 'MyClass' object has no attribute 'value'
obj.value = 42

# Example 6: Data Cleanup
'''
Data Cleanup: In data processing tasks, you might create temporary attributes for intermediate results. 
Once these attributes are no longer needed, you can use delattr() to clean up the object.
'''

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        # Process data and store intermediate results
        self.result = self.data * 2

    def cleanup(self):
        # Remove intermediate results
        delattr(self, 'result')

processor = DataProcessor(10)
processor.process_data()

# Do something with intermediate result

# Cleanup to remove intermediate result attribute
processor.cleanup()


# Example 6: Security
'''
In some security-sensitive applications, you may need to remove sensitive information from objects to prevent unauthorized access.
'''
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def logout(self):
        # Remove password attribute to enhance security
        delattr(self, 'password')

user = User("example_user", "secure_password")

# Perform logout operation
user.logout()

