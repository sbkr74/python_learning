# string
string = "Python Programming from basic to advance"
s = slice(7,19)
print(string[s])                # Output: Programming

# list
myList = string.split(' ')
l = slice(1,6,2)
print(myList[l])                # Output: ['Programming', 'basic', 'advance']

# tuple
my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
s = slice(1, 7, 2)
print(my_tuple[s])              # Output: (1, 3, 5)


# Using slice() with indices()
'''
The indices() method of the slice object returns a tuple containing the start, stop, 
and step values as per the length of the sequence.'''
my_slice = slice(1, 10, 2)
print(my_slice.indices(20))     # Output: (1, 10, 2)

for i in range(*my_slice.indices(20)):
    print(i, end=" ")           # Output: 1 3 5 7 9
