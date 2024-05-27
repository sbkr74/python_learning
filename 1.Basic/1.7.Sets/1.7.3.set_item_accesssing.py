# How we can access items in set
st = {'item1','item2','item3','item4','item5','item7'}
print(st)

for items in st:
    print(items)

##########################################################################
# 1. Using itertools.islice
'''
The itertools.islice function allows you to create an iterator that returns selected elements from the input iterable. 
This can be useful to fetch a specified number of items from a set.
'''
import itertools

my_set = {1, 2, 3, 4, 5}
n = 4  # Number of items to fetch

few_items = set(itertools.islice(my_set, n))
print(few_items)

# 2. Using set comprehension with enumerate
'''
You can use a set comprehension along with the enumerate function to fetch a specified number of items from a set.
'''
st = {'item1','item2','item3','item4','item5','item7'}
n = 3
some_items = {item for i,item in enumerate(st) if i<n}
print(some_items)

##########################################################

# 3. Using a for loop
'''You can also use a simple for loop to fetch a specified number of items from a set.'''
my_set = {1, 2, 3, 4, 5}
n = 3  # Number of items to fetch
few_items = set()
for i, item in enumerate(my_set):
    if i >= n:
        break
    few_items.add(item)

print(few_items)
