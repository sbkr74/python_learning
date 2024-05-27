whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
diff_num = whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}
print(diff_num)
python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.difference(dragon))     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
print(dragon.difference(python))     # {'d', 'r', 'a', 'g'}

########################################################
# Finding Symmetric Difference Between Two Sets
'''
It returns the the symmetric difference between two sets. 
It means that it returns a set that contains all items from both sets, 
except items that are present in both sets, mathematically: (A\B) ∪ (B\A)
'''

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers)) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.symmetric_difference(dragon))  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}

   