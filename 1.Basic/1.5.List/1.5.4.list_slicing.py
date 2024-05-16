# Slicing items
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits_end = fruits[0:4] # it returns all the fruits
# this is also give the same result as the above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the end index
orange_mango_lemon = fruits[1:]

# printing the results
print("All Fruits using end index:",all_fruits_end)
print("All fruits:",all_fruits)
print(orange_and_mango)
print(orange_mango_lemon)

fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[-4:] # it returns all the fruits
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1] # it does not include the end index
orange_mango_lemon = fruits[-3:]
print("All fruits:",all_fruits)
print(orange_and_mango)
print(orange_mango_lemon)
