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


################################################################################
# Example: Checking Configuration Settings
class Config:
    def __init__(self, interest_rate=None, inflation_rate=None, tax_rate=None):
        self.interest_rate = interest_rate
        self.inflation_rate = inflation_rate
        self.tax_rate = tax_rate

# Create a configuration object with some settings
config = Config(interest_rate=0.05, tax_rate=0.15)

def get_config_value(config, setting):
    if hasattr(config, setting):
        return getattr(config, setting)
    else:
        return 'Setting not found'

# Example usage
settings_to_check = ['interest_rate', 'inflation_rate', 'tax_rate']

for setting in settings_to_check:
    value = get_config_value(config, setting)
    print(f"{setting}: {value}")

