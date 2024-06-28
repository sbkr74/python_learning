# The type() function in Python can be used in two ways:
'''1 . type() : return type(datatype) of an object.'''
s = "Python"
print(type(s))

##############################
'''2. To dynamically create a new class.'''
'''
Parameters
name: The name of the new class.
bases: A tuple containing the base classes from which the new class will inherit.
dict: A dictionary containing attributes and methods of the new class.
**kwds: Optional keyword arguments that allow additional metadata or behavior to be specified.
'''
# Define the parameters
class_name = 'MyClass'
base_classes = (object,)
class_attributes = {
    'attribute': 'value',
    'method': lambda self: "Hello, World!"
}
class_kwargs = {
    '__module__': __name__
}

# Create the class
MyClass = type(class_name, base_classes, class_attributes)

# Test the dynamically created class
instance = MyClass()
print(instance.attribute)  # Output: value
print(instance.method())   # Output: Hello, World!
