# The issubclass() function is used to check if a class is considered a subclass of another class. 

class BaseClass:
    pass

class DerivedClass(BaseClass):
    pass

class SecDevClass(BaseClass):
    pass

# Check if DerivedClass is a subclass of BaseClass
print(issubclass(DerivedClass, BaseClass))  # Output: True

# Check if SecDevClass is a subclass of BaseClass
print(issubclass(SecDevClass, BaseClass))  # Output: True

# Check if BaseClass is a subclass of DerivedClass
print(issubclass(BaseClass, DerivedClass))  # Output: False
