# Create empty Tuple
my_tuple = ()
print(type(my_tuple))
sec_tup = tuple()
print(type(sec_tup))

# creating tuple with items
ele_tup = ('Java', 'Python', 'Scala', 'SQL')
print(ele_tup)

# using map function
a,b,c = 10,20,30
map_tup = tuple(map(int,(a,c,b)))
print(map_tup)