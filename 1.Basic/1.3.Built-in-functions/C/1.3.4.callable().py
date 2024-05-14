def square(x):
    return x*x

def example():
    pass

print(callable(square))
print(callable(example))
print("==================================================================")

# Define a function
def greet():
    print("Hello!")

# Define a class with a __call__ method
class Greeter:
    def __call__(self):
        print("Hello from the Greeter class!")

# Define a regular object
class NotCallable:
    pass

# Create an instance of the class
obj = NotCallable()

# Check if objects are callable
print(callable(greet))       # Output: True
print(callable(Greeter()))   # Output: True
print(callable(NotCallable)) # Output: True

# Check if the instance is callable
print(callable(obj))  # Output: False
