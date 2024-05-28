# To check if an item exist in a list we use in membership operator
st = {'item1','item2','item3','item4','item5','item7'}
print("Does set contain item3?",'item3' in st)
print("Does set contain item6?",'item6' in st)

if 'item6' in st:
    print("item present in set")
else:
    print("item not found!")

# Checking Subset and Super Set
'''
A set can be a subset or super set of other sets:
Subset: issubset()
Superset: issuperset()
'''
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issubset(even_numbers)) # False, because it is a super set
print(whole_numbers.issuperset(even_numbers)) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.issubset(dragon))    # False

# Checking joining set have any common item
'''
If two sets do not have a common item or items we call them disjoint sets. 
We can check if two sets are joint or disjoint using isdisjoint() method.
'''
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers)) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.isdisjoint(dragon))  # False, there are common items {'o', 'n'}