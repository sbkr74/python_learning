# Create a new dictionary. The dict object is the dictionary class.

# 1. Creating a dictionary using keyword arguments:
my_dict = dict(name='John', age=30, city='New York')
print(my_dict)

# 2. Creating a dictionary from a list of tuples:
items = [('name', 'John'), ('age', 30), ('city', 'New York')]
my_dict = dict(items)
print(my_dict)

# 3. Creating a dictionary from two lists:
keys = ['name', 'age', 'city']
values = ['John', 30, 'New York']
my_dict = dict(zip(keys, values))
print(my_dict)

# 4 . Creating a dictionary from another dictionary:
old_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
my_dict = dict(old_dict)
print(my_dict)
