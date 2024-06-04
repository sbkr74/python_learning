'''
The iter() function is used to get an iterator from an iterable object, like a list, tuple, or string. 
An iterator is an object that allows you to traverse through all the elements of a collection, one element at a time.
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
