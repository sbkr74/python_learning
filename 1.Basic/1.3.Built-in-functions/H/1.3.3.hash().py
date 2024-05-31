'''
Return the hash value of the object. Hash values are integers. 
They are used to quickly compare dictionary keys during a dictionary lookup. 
Numeric values that compare equal have the same hash value 
(even if they are of different types, as is the case for 1 and 1.0).
'''
# Hashing integer
i = 22
i = str(i)
print(hash(i))

# Hashing integer
j = '22'
print(hash(j))

# checking
print(hash(i) == hash(j))

# Hashing string
s = "I am a Python Developer"
print(hash(s))

# Hashing a tuple
tuple_hash = hash((1, 2, 3))
print(tuple_hash)  # Output: A consistent integer hash value
