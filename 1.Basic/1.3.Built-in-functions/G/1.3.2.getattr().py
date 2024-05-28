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
