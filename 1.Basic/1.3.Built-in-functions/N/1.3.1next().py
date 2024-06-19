 # Creating an iterator from a list
my_list = [1, 2, 3]
iterator = iter(my_list)

# Using next() to get items from the iterator
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3

'''If we call next() again, it will raise StopIteration because the iterator is exhausted'''
# print(next(iterator))  # This will raise StopIteration

'''We can provide a default value to next() to avoid the StopIteration exception when the iterator is exhausted.'''
iterator = iter(my_list)

print(next(iterator, 'default'))  # Output: 1
print(next(iterator, 'default'))  # Output: 2
print(next(iterator, 'default'))  # Output: 3
print(next(iterator, 'default'))  # Output: default

'''Using next() in a Loop
In practice, iterating through an iterator is often done using a loop, which internally uses next().'''
iterator = iter(my_list)

for item in iterator:
    print(item)
'''This loop is equivalent to manually calling next() until a StopIteration exception is raised.'''

