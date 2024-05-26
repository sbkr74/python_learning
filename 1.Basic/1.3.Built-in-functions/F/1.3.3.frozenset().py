# Creating a frozenset from a list
my_frozenset = frozenset([1, 2, 3, 4, 5])
print(my_frozenset)

# Creating a frozenset from a tuple
fs = frozenset((1, 2, 3, 4, 5))
print(fs)

a = frozenset([1, 2, 3, 4])
b = frozenset([3, 4, 5, 6])

# Union
print(a | b)  # frozenset({1, 2, 3, 4, 5, 6})

# Intersection
print(a & b)  # frozenset({3, 4})

# Difference
print(a - b)  # frozenset({1, 2})

# Symmetric Difference
print(a ^ b)  # frozenset({1, 2, 5, 6})
