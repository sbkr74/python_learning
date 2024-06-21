class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

# Create an instance of Person
person = Person("Alice", 30)

# Use repr() to get the official string representation
print(repr(person))  # Output: "Person(name='Alice', age=30)"
