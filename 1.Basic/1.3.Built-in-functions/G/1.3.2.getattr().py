'''
getattr() function in Python is used to retrieve the value of an attribute from an object dynamically.
'''
# getattr(object, name[, default])      # syntax

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of Person
person = Person("Alice", 30)
#############################################
'''Example 1: Using Default Value'''
# Accessing a non-existent attribute with a default value
nickname = getattr(person, 'nickname', 'No nickname')
print(nickname)

#############################################
'''Example 2: Attribute Access'''
# Access attributes using getattr()
name = getattr(person, 'name')
age = getattr(person, 'age')

print(f"Name: {name}, Age: {age}")

'''Real-Life Scenario: Dynamic Configuration Access'''
class Config:
    def __init__(self):
        self.interest_rate = 0.05
        self.inflation_rate = 0.02
        self.tax_rate = 0.15

# Create a configuration object
config = Config()

# Function to dynamically access configuration settings
def get_config_value(config, setting):
    return getattr(config, setting, 'Setting not found')

# Example usage
settings_to_access = ['interest_rate', 'inflation_rate', 'non_existent_setting']

for setting in settings_to_access:
    value = get_config_value(config, setting)
    print(f"{setting}: {value}")

'''Advance Use-case: Using getattr() with Methods'''
class MathOperations:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

# Create an instance of MathOperations
math_ops = MathOperations()

# Function to dynamically call a method
def dynamic_method_call(obj, method_name, *args):
    method = getattr(obj, method_name, None)
    if method:
        return method(*args)
    else:
        return "Method not found"

# Example usage
result_add = dynamic_method_call(math_ops, 'add', 5, 3)
result_multiply = dynamic_method_call(math_ops, 'multiply', 5, 3)
result_non_existent = dynamic_method_call(math_ops, 'subtract', 5, 3)

print(f"Add: {result_add}")
print(f"Multiply: {result_multiply}")
print(f"Non-existent method: {result_non_existent}")
