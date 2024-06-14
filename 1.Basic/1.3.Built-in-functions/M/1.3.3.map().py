# map(function, iterable, *iterables)
numbers = [1, 2, 3, 4, 5]

# Using map() to convert each number to a string
string_numbers = map(str, numbers)

string_list = list(string_numbers)
print(string_list)  # Output: ['1', '2', '3', '4', '5']
##################################################################
numbers = [1, 2, 3, 4, 5]

# Using map() to apply a function to each item
squared = map(lambda x: x**2, numbers)

# Convert the map object to a list to see the results
squared_list = list(squared)
print(squared_list)  # Output: [1, 4, 9, 16, 25]
