# create an empty dictionary
myDict = {}
my_dict =  dict()

# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

# Printing statements
print(dct)
for ele in dct:
    print(dct.get(ele))
for key in dct.keys():
    print(key)
for key,value in dct.items():
    print(value)

person = {
    'first_name':'xyz',
    'last_name':'abc',
    'age':60,
    'country':'India',
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Somewhere in India',
        'zipcode':'888888'
    }
    }
print(person)