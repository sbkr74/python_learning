# The list() function in Python is used to create a list object. A list in Python is an ordered collection of items 
# which can be of different types, and it is mutable, meaning its contents can be changed.

# From a string
string = "hello"
list_from_string = list(string)         
print(list_from_string)                     # Output: ['h', 'e', 'l', 'l', 'o']

# From a tuple
tuple_example = (1, 2, 3)
list_from_tuple = list(tuple_example)           
print(list_from_tuple)                      # Output: [1, 2, 3]

# From a set
set_example = {1, 2, 3}
list_from_set = list(set_example)               
print(list_from_set)                        # Output: [1, 2, 3] (order may vary)

# From a dictionary (keys only)
dict_example = {'a': 1, 'b': 2}
list_from_dict = list(dict_example)             
print(list_from_dict)                       # Output: ['a', 'b']

list_comprehension = [x * 2 for x in range(5)]
print(list_comprehension)                   # Output: [0, 2, 4, 6, 8]
