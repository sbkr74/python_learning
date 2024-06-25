The `setattr()` function in Python is used to set the value of an attribute of an object. If the attribute does not exist, `setattr()` creates the attribute and assigns the specified value to it.

### Syntax
```python
setattr(object, name, value)
```
- `object`: The object whose attribute you want to set.
- `name`: The name of the attribute you want to set. This should be a string.
- `value`: The value you want to assign to the attribute.

### Examples

#### Basic Usage
```python
class Person:
    pass

# Create an instance of Person
person = Person()

# Set attributes using setattr()
setattr(person, 'name', 'Shubham Biruly')
setattr(person, 'age', 25)

# Access the attributes to verify
print(person.name)  # Output: Shubham Biruly
print(person.age)   # Output: 25
```

#### Using `setattr()` with a List of Attributes
If you have a list of attributes and values, you can use a loop to set multiple attributes dynamically.
```python
class Car:
    pass

# Create an instance of Car
car = Car()

# List of attributes and values
attributes = {
    'make': 'Toyota',
    'model': 'Corolla',
    'year': 2020,
    'color': 'Blue'
}

# Set the attributes using setattr()
for attr, value in attributes.items():
    setattr(car, attr, value)

# Access the attributes to verify
print(car.make)   # Output: Toyota
print(car.model)  # Output: Corolla
print(car.year)   # Output: 2020
print(car.color)  # Output: Blue
```

#### Modifying Existing Attributes
You can also use `setattr()` to modify existing attributes of an object.
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Create an instance of Book
book = Book("1984", "George Orwell")

# Modify the attributes using setattr()
setattr(book, 'title', 'Animal Farm')
setattr(book, 'author', 'George Orwell')

# Access the attributes to verify
print(book.title)   # Output: Animal Farm
print(book.author)  # Output: George Orwell
```

#### Handling Non-existent Attributes
If you try to set an attribute that doesn't exist, `setattr()` will create it.
```python
class Employee:
    def __init__(self, name):
        self.name = name

# Create an instance of Employee
employee = Employee("John Doe")

# Set a new attribute using setattr()
setattr(employee, 'position', 'Developer')

# Access the new attribute to verify
print(employee.position)  # Output: Developer
```

### Practical Example
A practical use case for `setattr()` might be when working with data that needs to be dynamically assigned to an object's attributes, such as when processing data from a JSON file or a configuration dictionary.

```python
class Config:
    def __init__(self, **entries):
        self.__dict__.update(entries)

# Example configuration data
config_data = {
    'host': 'localhost',
    'port': 8080,
    'debug': True
}

# Create a Config object and set attributes dynamically
config = Config(**config_data)

# Access the attributes to verify
print(config.host)  # Output: localhost
print(config.port)  # Output: 8080
print(config.debug) # Output: True
```

In summary, `setattr()` is a versatile function for dynamically setting attributes on objects, making it especially useful in scenarios where the attributes and their values are not known beforehand and need to be assigned at runtime.