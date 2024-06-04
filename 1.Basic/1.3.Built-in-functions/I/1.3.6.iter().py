'''
The iter() function is used to get an iterator from an iterable object, like a list, tuple, or string. 
An iterator is an object that allows you to traverse through all the elements of a collection, one element at a time.
'''

'''
The iter() function is a fundamental part of Python's iterator protocol and is used implicitly in loops and comprehensions to create an iterator object from an iterable. 
It's a powerful tool for creating custom iteration behaviors in your classes by defining __iter__() and __next__() methods.
'''
# Define a list
my_list = [1, 2, 3, 4]

# Get an iterator using iter()
my_iterator = iter(my_list)

# Iterate through it using next()
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3
print(next(my_iterator))  # Output: 4

# The following will raise a StopIteration error as the iterator is exhausted
# print(next(my_iterator))

'''
The iter() function can also be used with a sentinel value, 
where the iteration will stop when the sentinel value is returned by the callable object passed to iter(). 
'''
# Define a simple generator
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

# Create an iterator that stops at 5
counter = count_up_to(5)
counter_iterator = iter(counter)

# Use next() to get the next item
print(next(counter_iterator))  # Output: 1
print(next(counter_iterator))  # Output: 2

# ... and so on until 5
