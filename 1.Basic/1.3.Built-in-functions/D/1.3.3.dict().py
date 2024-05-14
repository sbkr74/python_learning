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

# few more examples
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
print(a==b==c==d==e==f)
'''
Dictionaries can be created by several means:

    Use a comma-separated list of key: value pairs within braces: {'jack': 4098, 'sjoerd': 4127} or {4098: 'jack', 4127: 'sjoerd'}

    Use a dict comprehension: {}, {x: x ** 2 for x in range(10)}

    Use the type constructor: dict(), dict([('foo', 100), ('bar', 200)]), dict(foo=100, bar=200)

'''