# Joining Sets
'''We can join two sets using the union() or update() method.'''

# union()
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3)

# update()
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2)
print(st1)

########################################################################
# intersection between two sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
even_numbers = {0, 2, 4, 6, 8, 10}
intersect = whole_numbers.intersection(even_numbers)
print(intersect)

python = {'p', 'y', 't', 'h', 'o','n'}
anaconda = {'a','n','a','c','o','n','d','a'}
intersect = python.intersection(anaconda) 
print(intersect) 

