# create an empty set
empty_set = set()
print(type(empty_set))

# create a set with elements 
my_set = {1,2,3,4,5}
print(type(my_set))
st = {'item1','item2','item3','item4','item5'}
print(type(st))

# using map function
a,b,c = 10,20,30
map_set = set(map(int,(a,c,b)))
print(type(map_set))