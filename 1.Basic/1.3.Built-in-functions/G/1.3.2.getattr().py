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

