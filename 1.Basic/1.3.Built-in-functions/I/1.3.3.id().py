'''
 id(object)

    Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object
    during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.
'''

# Example 1: Getting the ID of an Integer
x = 12
print(id(x))  # Output: The unique identifier of the integer object.

# Example 2: Getting the ID of a String
s = "Python"
print(id(s))  # Output: The unique identifier of the string object.

# Example 3: Getting the ID of a List
lst = [1, 2, 3]
print(id(lst))  # Output: The unique identifier of the list object
####################################################################################################################

'''Real-Life Scenario: Understanding Object Mutability'''
# Example: Comparing Mutable and Immutable Objects
# Immutable object example (integers)
a = 10
b = 10
print(id(a) == id(b))  # Output: True, because integers are immutable and can share the same ID

# Mutable object example (lists)
lst1 = [1, 2, 3]
lst2 = [1, 2, 3]
print(id(lst1) == id(lst2))  # Output: False, because lists are mutable and have different IDs

# Changing an element in a list
lst1[0] = 4
print(id(lst1))
print(lst1)  # Output: [4, 2, 3]
print(id(lst1))  # Output: ID remains the same
