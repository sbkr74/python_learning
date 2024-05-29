person = {
    'first_name':'xyz',
    'last_name':'abc',
    'age':60,
    'country':'India',
    'skills':['JavaScript', 'React', 'Python', 'MongoDB', 'Node'],
    'address':{
        'street':'Somewhere in India',
        'zipcode':'888888'
    }
    }

# accessing items from dictionary
# we can acess item using its key.
print(person['age'])
print(person['country'])
print(person['skills'][2])
print(person['address']['zipcode'])
# print(person['city'])                           # keyError

# if key is not present then we will get key error. if we are accesing using keys
# Alternative is get()
print("\nUsing get():")
print(person.get('age'))
print(person.get('skills')[2])
print(person.get('city'))

# accessing all keys of dictionary
keys = person.keys()
print(keys)

# accessing all values in dictionary
values = person.values()
print(values)