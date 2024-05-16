# list can be deined in several ways

# To create a empty list
# 1. using list symbol
myList = []
print(type(myList))

# 2. using list() function to create empty list
list1 = list()
print(type(list1))

# 3. using elements then map them into list
a,b,c = 10,20,30
x = list(map(int,(a,b,c)))
print(x)

# 4. using elements
fruits = ['banana', 'orange', 'mango', 'lemon']                         # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']          # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']                 # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB']    # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']       # list of countries

# Print the lists
print('Fruits:', fruits)
print('Vegetables:', vegetables)
print('Animal products:',animal_products)
print('Web technologies:', web_techs)
print('countries:', countries)
