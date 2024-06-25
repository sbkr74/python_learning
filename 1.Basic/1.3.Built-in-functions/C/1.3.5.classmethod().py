'''
It's commonly used to define methods that act on the class itself or on class-level data.
The primary use cases for classmethod() include:
    1.) Alternative Constructors: Class methods can be used as alternative constructors. 
        For example, a class method can parse a string and create an instance of the class based on the parsed data.
    2.) Factory Methods: They can act as factory methods that return instances of the class based on certain conditions.
    3.) Accessing Class Variables: They are useful for accessing or modifying class variables that are 
        shared among all instances of the class.
'''
class MyClass:
    class_variable = 10

    # def __init__(self, x):
    #     self.x = x

    @classmethod
    def class_method(cls):
        print("This is a class method")
        print("Class variable:", cls.class_variable)

# Call the class method without creating an instance
MyClass.class_method()

################################################
class MathUtils:
    _factor = 5

    @classmethod
    def multiply(cls, a):
        return a * cls._factor

# Call the class method without creating an instance
print(MathUtils.multiply(5))  # Output: 25
