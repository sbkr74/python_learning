# dict or dictionary datatype store the item in key:value pair
# where key can't be duplicate but values can
# dict is mutable in nature and order are not preserved.

d = {1:'python',2:'program',3:'Basic',4:'python'}
print(type(d))
print(d)

#printing value using key of dict
print(d[2])

# Assigning new value to key
d[4] = 'Advance'
print(d)

#we can also add key-value pair
d[5] = 101
print(d)